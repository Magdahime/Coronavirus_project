import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


def get_rows(data_frame, top10):

    cases_list =[]
    for region in top10:
        new_data_frame = data_frame.loc[data_frame["Country/Region"]==region]
        formatteddf = new_data_frame.groupby(by='Country/Region').sum()
        cases_list.append(formatteddf.loc[region].tolist())
    
    return cases_list


def get_dates(data_frame):

    return data_frame.columns.tolist()[1:]


def draw_graph(plots, title, disease, ticks):
    x_axis, x_axis_name, y1_axis, y2_axis, y_axis_name = plots
    plt.style.use('seaborn')
    fig = plt.figure(dpi=128, figsize=(20, 10))
    plt.ylim(auto=True)
    plt.plot(x_axis, y1_axis, c='purple', linewidth=2.0, label="Cases")
    plt.plot(x_axis, y2_axis, c='red', linewidth=2.0, label='Deaths')
    plt.legend()
    plt.fill_between(x_axis, y1_axis, y2_axis, facecolor='blue', alpha=0.1)
    #SHOWNG ONLY THE 7TH LABEL
    frame1 = plt.gca()
    labels = [label.set_visible(False) for label in frame1.axes.get_xticklabels()]
    labels = [label.set_visible(True) for label in frame1.axes.get_xticklabels()[::ticks]]
    plt.title(title, fontsize=24)
    plt.xlabel(x_axis_name, fontsize=20)
    fig.autofmt_xdate()
    plt.ylabel(y_axis_name, fontsize=20)
    plt.yscale(value="log")
    plt.tick_params(axis='both', which='major', labelsize=10)
    save_filename = title
    plt.savefig(f'output/{disease}/' + save_filename, bbox_inches='tight')


def get_top10(data_frame, parameter, dates):
    data_frame = data_frame.sort_values(by = [dates, parameter], ascending=False)
    return data_frame["Country"].tolist()[:10]


def format_data(data_frame, region, disease, str_dates, str_cases, str_deaths):
    
    data_frame = data_frame.loc[data_frame["Country"]==region]
    cases = data_frame[str_cases]
    deaths = data_frame[str_deaths]
    dates = data_frame[str_dates]
    return (cases, deaths, dates, disease)
    
def format_sars(data_frame):

    str_cases = "Cumulative number of case(s)"
    str_dates = "Date"
    top10 = get_top10(data_frame, str_cases, str_dates)
    for region in top10:
        graph_sars(data_frame, region, str_cases, str_dates)


def format_swine_flu(data_frame):

    str_cases = "Cases"
    str_dates = "Update Time"
    top10 = get_top10(data_frame, str_cases, str_dates)
    for region in top10:
        graph_swine_flu(data_frame, region, str_cases, str_dates)


def graph_swine_flu(data_frame, region, str_cases, str_dates):
 
    cases, deaths, dates, disease = format_data(data_frame, region, "Swine flu", str_dates,
                                                str_cases, "Deaths")
    plots = (dates, "Dates", cases, deaths, "Cases and deaths")
    draw_graph(plots, f"Cases of Swine flu in {region}", disease, 2)



def graph_sars(data_frame, region, str_cases, str_dates):

    cases, deaths, dates, disease = format_data(data_frame, region, "SARS", str_dates, str_cases, "Number of deaths")
    plots = (dates, "Dates", cases, deaths, "Cases and deaths")
    draw_graph(plots, f"Cases of SARS in {region}", disease, 7)


def format_corona(data_frames):
    data_frame_c, data_frame_d = data_frames
    data_frame_c = data_frame_c.drop(["Province/State", "Lat", "Long"], axis="columns")
    data_frame_d = data_frame_d.drop(["Province/State", "Lat", "Long"], axis="columns")
    dates = get_dates(data_frame_c)
    last_date = dates[-1]
    top10 = data_frame_c.sort_values(by = last_date, ascending = False)["Country/Region"].head(10).tolist()
    deaths = get_rows(data_frame_d, top10)
    cases = get_rows(data_frame_c, top10)
    for country in range(len(top10)):
        plots = ((dates, "Dates", cases[country],
               deaths[country], "Cases and deaths"))
        draw_graph(plots, f"Cases of COVID-19 in {top10[country]}","COVID-19",7)

def unpack(list1, list2, value1, value2):
    list3 = []
    for x in range(len(list1)):
        list3.append((list1[x], list2[x], value1, value2))
    return list3


def gather_data(dfcorona, dfsars, dfswine):
    dfcorona_cases, dfcorona_deaths = dfcorona
    SARS = []
    SWINE = []
    dates = get_dates(dfcorona_cases)
    last_date = dates[-1]
    top10 = dfcorona_cases.sort_values(by = last_date, ascending = False)["Country/Region"].head(10).tolist()
    for region in top10:
        SARS.append(format_data(dfsars, region, "SARS", "Date", "Cumulative number of case(s)", "Number of deaths"))
        SWINE.append(format_data(dfswine, region, "Swine flu", "Update Time", "Cases", "Deaths"))
    cases = get_rows(dfcorona_cases, top10)
    deaths = get_rows(dfcorona_deaths, top10)
    CORONA = unpack(cases, deaths, dates, "COVID-19")
    
    for region in range(len(top10)):
        format_together(SARS[region], SWINE[region], CORONA[region], top10[region])

def graph_compare(x_ax, y1_ax, y2_ax, y3_ax, title):
    x_axis, x_axis_name = x_ax
    y1_values, descritption1 = y1_ax
    y2_values, description2 = y2_ax
    y3_values, description3 = y3_ax
    plt.style.use('bmh')
    fig = plt.figure(dpi=128, figsize=(20, 10))
    plt.plot(x_axis, y1_values, c='purple', linewidth=2.0, label=descritption1)
    plt.plot(x_axis, y2_values, c='green', linewidth=2.0, label=description2)
    plt.plot(x_axis, y3_values, c='red', linewidth=2.0, label=description3)
    plt.legend()
    plt.title(title, fontsize=24)
    plt.xlabel(x_axis_name, fontsize=20)
    fig.autofmt_xdate()
    plt.ylabel("", fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=10)
    save_filename = title
    plt.savefig(f'output/compare/' + save_filename, bbox_inches='tight')



def format_together(disease1, disease2, disease3, region):
    cases1, deaths1, dates1, name1 = disease1
    cases2, deaths2, dates2, name2 = disease2
    cases3, deaths3, dates3, name3 = disease3
    if len(cases1) == 0 or len(cases2) == 0 or len(cases3) == 0:
        return
    if len(deaths1) == 0 or len(deaths2) == 0 or len(deaths3) == 0:
        return
    else:
        max_dates = min([len(dates1), len(dates2), len(dates3)])
        dates = [x for x in range(1, max_dates+1)]
        graph_compare((dates, "Days of pandemia"),
                    (cases1[:max_dates], name1), (cases2[:max_dates], name2),
                    (cases3[:max_dates], name3),
                    f"Graph comparing development of three viral diseases in {region}")
        graph_compare((dates, "Days of pandemia"),
                    (deaths1[:max_dates], name1), (deaths2[:max_dates], name2),
                    (deaths3[:max_dates], name3), 
                    f"Graph comparing death rate of three viral diseases in {region}")
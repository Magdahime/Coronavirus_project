import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
    plt.ylabel("", fontsize=20)
    plt.yscale(value="log")
    plt.tick_params(axis='both', which='major', labelsize=10)
    save_filename = title
    plt.savefig(f'output/{disease}/' + save_filename, bbox_inches='tight')


def get_top10(data_frame, parameter, dates):
    data_frame = data_frame.sort_values(by = [dates, parameter], ascending=False)
    return data_frame["Country"].tolist()[:10]

def format_data(data_frame, region, disease, dates, cases, deaths, ticks):
    
    data_frame = data_frame.loc[data_frame["Country"]==region]
    plots = (data_frame[dates],"Dates", data_frame[cases],
               data_frame[deaths], "Cases and deaths")
    draw_graph(plots, f"Cases of {disease} in {region}", disease, ticks)

def format_swine_flu(data_frame):
    cases = "Cases"
    dates = "Update Time"
    top10 = get_top10(data_frame, cases, dates)
    for region in top10:
        format_data(data_frame, region, "Swine flu", dates,
                    cases, "Deaths", 2)


def format_sars(data_frame):
    cases = "Cumulative number of case(s)"
    dates = "Date"
    top10 = get_top10(data_frame, cases, dates)
    for region in top10:  
        format_data(data_frame, region, "SARS", dates,
                    cases, "Number of deaths", 7)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def draw_graph(plots, title):
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
    labels = [label.set_visible(True) for label in frame1.axes.get_xticklabels()[::7]]
    plt.title(title, fontsize=24)
    plt.xlabel(x_axis_name, fontsize=20)
    fig.autofmt_xdate()
    plt.ylabel("", fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=10)
    save_filename = title
    plt.savefig('output/' + save_filename, bbox_inches='tight')


def get_top10(data_frame, parameter):
    data_frame = data_frame.sort_values(by = ["Date", parameter], ascending=False)
    return data_frame["Country"].tolist()[:10]

def format_sars(data_frame):
    print("Countries with most cases of SARS:")
    cases = "Cumulative number of case(s)"
    top10 = get_top10(data_frame, cases)
    for country in top10:
        print(f"- {country}")
    data_frame = data_frame.loc[data_frame["Country"]=="China"]
    plots = (data_frame["Date"],"Dates", data_frame[cases],
               data_frame["Number of deaths"], "Cases and deaths")
    draw_graph(plots, "Cases of SARS in China")

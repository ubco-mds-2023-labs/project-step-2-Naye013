from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from tabulate import tabulate
import pandas as pd
import numpy as np

class Performance_Analyzer:
    """
    Performance_Analyzer class helps to provide summary on statistics metrics and visualize the charts.
    
    It generates the following visualizations and call basic metrics to display in console and export in a PDF file the following:
    1. Histogram
    2. Bar plot
    3. Line chart
    4. Box plot
    5. Scatter plot
    6. Metrics like mean, median, mode, count, max, min
    
    Parameters:
        config: Configuration
            An object from the Configuration class containing configuration settings.
    """
    def __init__(self, config):
        """
        Initializes the Performance_Analyzer.

        Parameters:
            config: Configuration
                An object from the Configuration class containing configuration settings.
        """
        self.config = config
        
    def __prepare_axis_components__(self, entity_collection, field):
        """
        Prepares data for plotting by extracting X and Y axis components.

        Parameters:
            entity_collection: EntityCollection
                A collection of entities with data to be analyzed.
            field: str
                The field for which the data is being prepared.

        Returns:
            list, list
                Returns chart_x_axis and chart_y_axis.
        """
        chart_x_axis = []
        chart_y_axis = []
        for entity in entity_collection.items:
            chart_x_axis.append(entity.entity_id)
            if field in entity.field_value_pairs:
                chart_y_axis.append(entity.field_value_pairs[field])
            else:
                chart_y_axis.append(0)

        return chart_x_axis, chart_y_axis

    def __generate_histogram__(self, x, y,title, xlabel,ylabel,ax=[0,0]):
        """
        Generates a histogram plot.

        Parameters:
            ax: AxesSubplot
                The subplot where the histogram will be plotted.
            x: list
                X-axis data.
            y: list
                Y-axis data.
        """
        #ax.hist(y, bins=10, edgecolor='black')
        plt.hist(y, bins=10)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def __generate_barplot__(self, x, y, title, xlabel, ylabel,ax=[0,0]):
        """
        Generates a bar plot.

        Parameters:
            ax: AxesSubplot
                The subplot where the histogram will be plotted.
            x: list
                X-axis data.
            y: list
                Y-axis data.
        """
        plt.bar(x, y)
        plt.show()

    def __generate_line_chart__(self, x, y, title, xlabel, ylabel,ax=[0,0]):
        """
        Generates a line chart.

        Parameters:
            ax: AxesSubplot
                The subplot where the histogram will be plotted.
            x: list
                X-axis data.
            y: list
                Y-axis data.
        """
        plt.plot(x, y, marker='o')
        plt.show()

    def __generate_boxplot__(self, x, y, title, xlabel, ylabel,ax=[0,0]):
        """
        Generates a box plot.

        Parameters:
            ax: AxesSubplot
                The subplot where the histogram will be plotted.
            x: list
                X-axis data.
            y: list
                Y-axis data.
        """
        plt.boxplot(y, vert=False)
        plt.show()

    def __generate_scatter_plot__(self, x, y, title, xlabel, ylabel,ax=[0,0]):
        """
        Generates a scatter plot.

        Parameters:
            ax: AxesSubplot
                The subplot where the histogram will be plotted.
            x: list
                X-axis data.
            y: list
                Y-axis data.
        """
        plt.scatter(x, y)
        plt.show()

    def summarize(self, entity_collection):
        """
        Helps to provide summary
        :param entity_collection: Entity Collection Object
        :return:None
        """
        LINE = "-----------------------------"
        xlabel = self.config.base_field
        for field in entity_collection.fields:
            ylabel = field
            print(LINE)
            print("Summary on {}".format(field))
            print(LINE)
            print("MEAN  : ", entity_collection.compute_mean(field))
            print("MODE  : ", entity_collection.compute_mode(field))
            print("MEDIAN: ", entity_collection.compute_median(field))
            print("MIN   : ", entity_collection.compute_min(field))
            print("MAX   : ", entity_collection.compute_max(field))
            print("COUNT : ", entity_collection.compute_count(field))
            print(LINE)
            print("VISUALIZATION")
            print(LINE)

            x, y = self.__prepare_axis_components__(entity_collection, field)

            self.__generate_line_chart__(x, y, "line chart", xlabel, ylabel)
            self.__generate_scatter_plot__(x, y, "scatter plot", xlabel, ylabel)
            self.__generate_boxplot__(x, y, "box plot", xlabel, ylabel)
            #self.__generate_histogram__(x, y, "Histogram", xlabel, ylabel)
            print(LINE)


            '''
    def summarize_and_export(self, entity_collection):
        xlabel = self.config.base_field

        """
        Summarizes data, display visualizations and summary table in the console and exports to a PDF file.

        Parameters:
            entity_collection: EntityCollection
                A collection of entities with data to be analyzed.
            pdf_filename: str
                The name of the PDF file to save the visualizations and summary table.
        """
        pdf_filename = "export.pdf" # datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".pdf"
        with PdfPages(pdf_filename) as pdf:
            LINE = "-----------------------------"
            for field in entity_collection.fields:
                xlabel = self.config.base_field
                ylabel = field
                # Create a 2x3 subplot grid
                fig, axs = plt.subplots(2, 3, figsize=(15, 10))

                # Display summary information in a table
                LINE = "-----------------------------"
                print(LINE)
                print("Summary on {}".format(field))
                print(LINE)
                print("MEAN  : ", entity_collection.compute_mean(field))
                print("MODE  : ", entity_collection.compute_mode(field))
                print("MEDIAN: ", entity_collection.compute_median(field))
                print("MIN   : ", entity_collection.compute_min(field))
                print("MAX   : ", entity_collection.compute_max(field))
                print("COUNT : ", entity_collection.compute_count(field))
                print(LINE)
                """summary_data = {
                    "COUNT": entity_collection.compute_count(field),
                    "MEAN": entity_collection.compute_mean(field),
                    "MODE": entity_collection.compute_mode(field),
                    "MEDIAN": entity_collection.compute_median(field),
                    "MIN": entity_collection.compute_min(field),
                    "MAX": entity_collection.compute_max(field),
                }
                table_data = tabulate(summary_data.items(), headers=["Metric", "Value"])
                axs[0, 0].axis('off')  # Hide axes for the table
                axs[0, 0].table(cellText=table_data,
                                cellLoc='center',
                                loc='center',
                                bbox=[0, 0, 1, 1])1"""

                # Prepare data for plots
                x, y = self.__prepare_axis_components__(entity_collection, field)

                # Display histogram
                self.__generate_histogram__(axs[0, 1], x, y, f'Histogram of {field}', xlabel, ylabel)

                # Display barplot
                self.__generate_barplot__(axs[0, 2], x, y, f'Bar Plot of {field}', xlabel, ylabel)

                # Display boxplot
                self.__generate_boxplot__(axs[1, 0], x, y, f'Box Plot of {field}', xlabel, ylabel)

                # Display line chart
                self.__generate_line_chart__(axs[1, 1], x, y, f'Line Chart of {field}', xlabel, ylabel)

                # Display scatter plot
                self.__generate_scatter_plot__(axs[1, 2], x, y, f'Scatter Plot of {field}', xlabel, ylabel)

                plt.suptitle(f"Summary and Visualizations for {field}", fontsize=16)
                plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to prevent overlap
                plt.show()

                # Save the current figure to the PDF
            pdf.savefig()

                # Display the complete layout
            plt.show()
            plt.close()

            print(f"Plots and table for {field} saved to {pdf_filename}")'''

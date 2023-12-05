
class Performance_Analyzer:
    """
    Performance_Analyzer class helps to provide summary on statistics metrics and visualize the charts
    In detail it helps to generate: -
    1. histogram
    2. heatmap
    3. boxplot
    4. linechart
    5. scatterplot
    6. basics metrics like mean, median, mode, count, max, min
    """
    def __init__(self, config):
        """
        Helps to initialize the class
        :param config: config object from Configuration class
        """
        self.config = config

    def __generate_histogram__(self, x, y):
        pass

    def __generate_heatmap__(self, x, y):
        pass

    def __generate_boxplot__(self, x, y):
        pass

    def __generate_line_chart__(self, x, y):
        pass

    def __generate_scatter_plot__(self, x, y):
        pass

    def export(self,entityCollection):
        pass
    def __prepare_axis_components__(self, entity_collection, field):
        chart_x_axis = []
        chart_y_axis = []
        for entity in entity_collection.items:
            chart_x_axis.append(entity.entity_id)
            if field in entity.field_value_pairs:
                chart_y_axis.append(entity.field_value_pairs[field])
            else:
                chart_y_axis.append(0)
        return chart_x_axis, chart_y_axis

    def summarize(self, entity_collection):
        LINE = "-----------------------------"
        for field in entity_collection.fields:
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
            x, y = self.__prepare_axis_components__(entity_collection,field)
            self.__generate_histogram__(x, y)
            self.__generate_heatmap__(x, y)
            self.__generate_boxplot__(x, y)
            self.__generate_line_chart__(x, y)
            self.__generate_scatter_plot__(x, y)
            print(LINE)





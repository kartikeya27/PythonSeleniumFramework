import pytest
import softest
from pages.launch_page import LaunchPage
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launchPage = LaunchPage(self.driver)
        self.utilPage = Utils()
    
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testdata.yaml")
    # @data(*Utils.read_data_from_excel("/Users/k-bhatt/PythonTestFrameworkDemo/testdata/tdataexcel.xlsx", "Sheet1"))
    # @data(*Utils.read_data_from_csv("/Users/k-bhatt/PythonTestFrameworkDemo/testdata/tdatacsv1.csv"))
    @data(*Utils.read_data_from_csv("/Users/k-bhatt/PythonTestFrameworkDemo/testdata/tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self,goingfrom, goingto, date, stops):
        # Provide going from location
        search_flight_result =  self.launchPage.searchFlights(goingfrom, goingto, date)
        
        # To handle dynamic scroll
        # self.launchPage.page_scroll()
        self.launchPage.wait_for_loading_indicator()
        # self.launchPage.page_scroll_to_bottom()
        self.launchPage.page_scroll()
        
        # Select the filter 1 stop
        search_flight_result.filter_flights_by_stop(stops)

        # Verify that the filtered results show flights having only 1 stop 
        allstops = search_flight_result.get_search_flights_results()
        self.log.info(len(allstops))
        
        self.utilPage.assertListItemText(allstops, stops)
        
    # def test_search_flights_2_stop(self):
    #     search_flight_result =  self.launchPage.searchFlights("New Delhi", "New York", "28/04/2024")
    #     self.launchPage.page_scroll()
    #     search_flight_result.filter_flights_by_stop("2 Stop")
    #     allstops = search_flight_result.get_search_flights_results()
    #     self.log.info(len(allstops))
    #     self.utilPage.assertListItemText(allstops, "2 Stops")
        
    # def test_search_flights_non_stop(self):
    #     search_flight_result =  self.launchPage.searchFlights("New Delhi", "New York", "28/04/2024")
    #     self.launchPage.page_scroll()
    #     search_flight_result.filter_flights_by_stop("Non Stop")
    #     allstops = search_flight_result.get_search_flights_results()
    #     self.log.info(len(allstops))
    #     self.utilPage.assertListItemText(allstops, "Non Stop")           
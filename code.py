from data_test.data_tester import data_test

if __name__ == '__main__':
    path_to_data = 'test/data/test_data_1.csv'
    tester = data_test(path_to_data)
    print(tester.see_data())
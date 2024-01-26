count = 1
while count < 49:
    try:
            xpath = '//*[@id="ctl00_CPH_Main_ctl00_RadGridFacturen_ctl00__' + str(x) + '"]/td[10]/input'
            time.sleep(2)
            driver.find_element_by_xpath(xpath).click()

    except NoSuchElementException:
            print('exception')
            nextPage = driver.find_element_by_xpath('//*[@id="ctl00_CPH_Main_ctl00_RadGridFacturen_ctl00"]/tfoot/tr/td/table/tbody/tr/td/div[3]/input[1]')
            nextPage.click()
            continue
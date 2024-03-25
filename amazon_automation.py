import rpa as r

def amazon_searchItem():
    r.init()

    # click on search bar and search for Iphone12 refurbished unlocked
    r.type('twotabsearchtextbox', 'iphone 12 refurbished unlocked')

    # print the searched up element
    searched_item = r.read('twotabsearchtextbox')
    print(searched_item)

    # perform the search by clicking on the search button
    r.click('nav-search-submit-button')

    # hold while amazon searches up the item
    # -10 second wait
    r.wait(10)

    # locate and click on the first item on the page
    first_item = 'B08PNM1LNZ'
    r.click(first_item)

    # wait for 5 seconds
    r.wait(5)

    # take a screenshot of the item
    r.snap('page', 'search_item_image.png')

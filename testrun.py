from sample_graphs import sum_and_product, sort_and_unique, replace_word, \
    scrape_image, http_fun

'''
g1 = sum_and_product.sum_and_product([1, 2, 3, 4])
output = g1.execute()


g2 = sort_and_unique.sort_and_unique('sample_graphs/testinput.txt',
                                    'sample_graphs/testoutput.txt')
g2.execute()



g3 = replace_word.replace_word('hello there my name is hello')
g3.execute()
g3 = replace_word.replace_word('the word you are looking for is not here')
g3.execute()


g4 = scrape_image.scraper_image('https://httpbin.org/image/png',
                                'sample_graphs/testscraped.png')
g4.execute()
'''

g5 = http_fun.test_post_graph('https://httpbin.org/post', dict(x=1, y=2))
g5.execute()

g6 = http_fun.test_get_graph('https://httpbin.org/get', dict(pippo=1, pluto="ciao"))
g6.execute()
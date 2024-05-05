import numpy as np


def simplex (f ,A , b ) :
    rows , cols = A . shape
    tab = np.column_stack (( A , np . eye ( rows ) ,b ) )
    f_mod = np.concatenate ((f , np . zeros ( rows +1) ) )# add zeros at end off to match dimensions
    tab = np . vstack (( tab , f_mod ) )# add f at the bottom of tab

    while True :

        last_row = tab [ -1]
        if min ( last_row [: len ( last_row ) -1]) >=0:# check main loop condition
            break
     # choosing the column with most negative end - row entry
    min_index_c = np . argmin ( last_row [0: len ( f ) ])# first part of last row that is actualy important
    # min_value_c = last_row [ min_index_c ]
    ratios = tab [0: rows , -1]/ tab [0: rows , min_index_c ]
    for i in range (0 , rows ) : # removing ratios corresponding to tab (1:r, min_index_c ) <= 0
        if tab [i , min_index_c ] <= 0:
            ratios [ i ] = 0
    min_ratio = min ( i for i in ratios if i > 0)# finding min ratio which is >0
    min_ratio_index = np . argwhere ( ratios == min_ratio )

    tab [ min_ratio_index ,:]= tab [ min_ratio_index ,]/ tab [min_ratio_index , min_index_c ]
    for i in range ( rows +1) :
        if i != min_ratio_index :
            tab [i ,] = tab [i ,] - tab [i , min_index_c ] * tab [min_ratio_index ,] # print (tab ,"\ n")
    x_final = np . zeros ( cols )
    tab_rows , tab_cols = tab . shape
    x_final = np . zeros ( cols )
    n = np . zeros ( cols )
    for i in range ( cols ) :
        v = tab [ np . nonzero ( tab [0: tab_rows , i ]) , i ]
        if( v . size == 1) :
            if( v == 1) :
                finding = np . argwhere ( tab [: , i ] ,)
                print (" find ", finding )
                x_final [ i ] = tab [ finding [0] , -1]
    return tab , x_final
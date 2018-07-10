import change_to_return as ctr


def test_calculate_change():
    change = ctr.calculate_change(10101,20000)
    assert change == 9899

def test_calc_change_items():
    change_desc = ctr.calc_change_items_to_return(10101,20000)
    assert change_desc == [ ('fifty', 1), ('twentys', 2), ('five', 1),
                            ('ones', 3), ('quarters', 3), ('dimes', 2),
                            ('pennys', 4) ]
ALPHA = 0.9 #коэффициент рождаемости молодняка у взрослых
BETA = 0.4 #коэффициент рождаемости молодняка у старых
DELTA = 0.7 #коэффициент выживаемости молодняка
RHO = 0.1 #коэффициент смертности старых животных
R_FOOD = 1500 # стоимость корма, необходимого взрослому животному в течение одного года

class Animal():
    """Summary
    Класс с животными, где хранятся данные о них

    Attributes:
        _young(int): количество молодых животных
        _adult(int): количество зрелых животных
        _old(int): количество старых животных
        _cur_years(int): количество лет до конца эксперимента
        _cur_amounts(int): всего животных на данный момент
        _year(int): текущий год

    """

    def __init__(self, diction, year):
        """Summary
        Инициализация данных
        """
        self._young = diction.get('y_amount')
        self._adult = diction.get('a_amount')
        self._old = diction.get('o_amount')
        self._cur_years = diction.get('ran_years')
        self._cur_amounts = diction.get('ran_amounts')
        self._year = year

    def count_newamount_animal(self):
        """Summary
        Функция подсчета новых животных по формулам
        """
        global ALPHA, BETA, DELTA, RHO
        _young_newamount = ALPHA * self._adult + BETA * self._old
        _adult_newamount = DELTA * self._young
        _old_newamount = self._adult + (1-RHO) * self._old

        if self._year in self._cur_years:
            _ind = self._cur_years.index(self._year)
            _young_newamount = _young_newamount * (100 - self._cur_amounts[_ind])/100
            _adult_newamount = _adult_newamount * (100 - self._cur_amounts[_ind])/100
            _old_newamount = _old_newamount * (100 - self._cur_amounts[_ind])/100

        return [_young_newamount, _adult_newamount, _old_newamount]

    def count_need_food(self):
        """Summary
        Функция подсчета нужного количества корма
        """
        global R_FOOD
        return R_FOOD * (self._young / 2 + self._adult + self._old / 3)

class Owner:
    """Summary
    Класс хозяина фермы, где хранятся данные о финансах

    Attributes:
        _young(int): количество молодых животных
        _adult(int): количество зрелых животных
        _old(int): количество старых животных
        _young_cost(int): цена за голову молодых животных
        _adult_cost(int): цена за голову зрелых животных
        _old_cost(int): цена за голову старых животных
        _young_sell(int): сколько нужно продать молодых животных
        _adult_sell(int): сколько нужно продать зрелых животных
        _old_sell(int): сколько нужно продать старых животных
        _cap(int): сейчас у хозяина имеется капитала
        _must_buyfood(int): нужно каждый год покупать корма для животных
        _cur_years(int): количество лет до конца эксперимента
        _cur_amounts(int): всего животных на данный момент
        _year(int): текущий год
        _penalty(int): штраф за неуплату по ферме

    """
    def __init__(self, diction, year):
        """Summary
        Инициализация класса
        """
        self._young = diction.get('y_amount')
        self._adult = diction.get('a_amount')
        self._old = diction.get('o_amount')
        self._young_cost = diction.get('young_cost')
        self._adult_cost = diction.get('adult_cost')
        self._old_cost = diction.get('old_cost')
        self._young_sell = diction.get('young_sell')
        self._adult_sell = diction.get('adult_sell')
        self._old_sell = diction.get('old_sell')
        self._cap = diction.get('capital')
        self._must_buyfood = diction.get('all_food')
        self._year = year
        self._penalty = diction.get('penalty')

    def check_penalty(self):
        """Summary
        Функция подсчета штрафа при продаже и покупке животных при просрочках
        """
        _penalty = 0
        if self._young < self._young_sell:
            _penalty += (self._young_sell - self._young) * self._penalty
        if self._adult < self._adult_sell:
            _penalty += (self._adult_sell - self._adult) * self._penalty
        if self._old < self._old_sell:
            _penalty += (self._old_sell - self._old) * self._penalty
        return _penalty

    def sell(self):
        """Summary
        Функция подсчета капитала хозяина при продаже и покупке животных с учетом штрафных санкций
        """
        if self._year == 0:
            capit = (self._cap - self._must_buyfood +
                     self._young_cost * self._young_sell + self._adult_cost * self._adult_sell +
                     self._old_cost * self._old_sell)
        else:
            capit = (self._cap - self._must_buyfood - self.check_penalty() +
                     self._young * self._young_cost + self._adult * self._adult_cost +
                     self._old * self._old_cost +
                     self._young_cost * self._young_sell + self._adult_cost * self._adult_sell +
                     self._old_cost * self._old_sell)
        return capit

    def paying_capacity(self):
        """Summary
        Функция измерения финансового положения хозяина
        """
        _flag = False
        _capit = self.sell()
        if _capit < 0: 
            _flag = True
        return _flag

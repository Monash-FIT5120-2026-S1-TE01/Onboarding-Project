"""
The core function implementation of true logic
"""

from typing import Callable, Optional, Any, Dict
from models import RecommendQuery

## TODO: Consider avoid **kwargs, using pydantic
class CalculateEngine:
    def __init__(self) -> None:
        self._func: Optional[Callable[[float], float]] = None

    def bind_func(
            self,
            func: Callable[[float], float] | str
    ) -> None:
        """
        Bind the function to the engine instance
        :param func: function or string to config of function
        """
        if isinstance(func, str):
            pass
        elif isinstance(func, Callable):
            self._func = func

    def cal(self, **kwargs) -> float:
        """
        The calculation logic implementation using the specify function
        """
        if self._func is None:
            raise ValueError("Please specify the function.")
        return self._func(**kwargs)

class RecommendEngine:
    def __init__(self) -> None:
        self._sql_head = """
            SELECT sugg_text
            FROM sugg_cloth
        """

    ## TODO: Determine the query SQL
    def build_sql(self, query: RecommendQuery) -> str:
        """
        Build SQL query base on conditions
        """
        active_filters = query.model_dump(exclude_unset=True) # Exclude those unset

        conditions = []
        for key, value in active_filters.items():
            conditions.append("<sql using marking method prevent sql insertion attach>")

        cond_sql = " AND ".join(conditions)
        sql = f"{self._sql_head} WHERE {cond_sql}"

        return sql

    ## TODO: Determine the connection to the database
    def recommend(self) -> str:
        """
        Recommend cloth base on the input condition
        """
        pass

if __name__ == "__main__":
    # Example usage for CalculateEngine
    cal_eng = CalculateEngine()
    cal_eng.bind_func(func=lambda x: x^2)
    result = cal_eng.cal()

    # Example usage for RecommendEngine
    rec_eng = RecommendEngine()
    rec_eng.build_sql(query=...)
    sugg_cloth = rec_eng.recommend()
from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate_review(
        self,
        code: str,
    ) -> str:
        pass
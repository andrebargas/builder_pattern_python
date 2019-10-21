from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
import datetime
import random

class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
            Concrete Builders are supposed to provide their own methods for
            retrieving results. That's because various types of builders may create
            entirely different products that don't follow the same interface.
            Therefore, such methods cannot be declared in the base Builder interface
            (at least in a statically typed programming language).

            Usually, after returning the end result to the client, a builder
            instance is expected to be ready to start producing another product.
            That's why it's a usual practice to call the reset method at the end of
            the `getProduct` method body. However, this behavior is not mandatory,
            and you can make your builders wait for an explicit reset call from the
            client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class ConcreteBuilderUsuario(Builder):
    """
    Implementacao da classe Builder para usuarios
    """

    def __init__(self) -> None:
        """
            Reinicia o construtor para que sempre tenha um novo produto quanso iniciada
        """
        self.reset()

    def reset(self) -> None:
        self._product = ProductUsuario()

    @property
    def product(self) -> ProductUsuario:
        
        """
        Metodo para obter o produto.Resetar o produto nao é algo obrigatório podendo ter uma funcao explicita para isso
        """
        product = self._product
        self.reset()
        return product


    def produce_part_a(self) -> None:
        self._product.addIp()

    def produce_part_b(self) -> None:
        self._product.addDateTime()

    def produce_part_c(self) -> None:
        self._product.addName()


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class ProductUsuario():
    """
    Produto para a representacao de usuario visitantes ou nao
    """

    def __init__(self) -> None:
        self.ip = None
        self.datetime = None
        self.name = None

    def addIp(self) -> None:
        self.ip = random.random()  * 100

    def addDateTime(self) -> None:
        self.datetime = datetime.datetime.now()

    def addName(self) -> None:
        self.name = "Andre"


    def showUser(self) -> None:
        if self.name:
            print(f" Ip: " + str(self.ip) + ";\n Data-Hora: " + str(self.datetime) + ";\n Nome: " + self.name)
        else :
            print(f" Ip: " + str(self.ip) + ";\n Data-Hora: " + str(self.datetime))



class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

    def build_usuario_visitante(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
    
    def build_usuario_registrado(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()



if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

    print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXX ")

    print("\nCriacao de Usuarios ")
    builder = ConcreteBuilderUsuario()
    director.builder = builder
    
    print("Usuario Visitante: ")
    director.build_usuario_visitante()
    builder.product.showUser()


    print("Usuario Registrado: ")
    director.build_usuario_registrado()
    builder.product.showUser()
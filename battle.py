from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory


def factory_test(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle_test(a: CreatureFactory, b: CreatureFactory) -> None:

    creature_a = a.create_base()
    creature_b = b.create_base()

    print("\nTesting battle")

    print(creature_a.describe())
    print("vs")
    print(creature_b.describe())

    print("fight!")

    print(creature_a.attack())
    print(creature_b.attack())


def main() -> None:
    flame = FlameFactory()
    factory_test(flame)

    aqua = AquaFactory()
    factory_test(aqua)

    battle_test(flame, aqua)


if __name__ == "__main__":
    main()

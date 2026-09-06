from ex1 import HealingCreatureFactory, TransformCreatureFactory

def main() -> None:
    healing_factory = HealingCreatureFactory()

    print("Testing Creature with healing capability")

    print("base:")
    base_healer = healing_factory.create_base()
    print(base_healer.describe())
    print(base_healer.attack())
    print(base_healer.heal())

    print("evolved:")
    evolved_healer = healing_factory.create_evolved()
    print(evolved_healer.describe())
    print(evolved_healer.attack())
    print(evolved_healer.heal())

    transforming_factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")

    print("base:")
    base_transformer = transforming_factory.create_base()
    print(base_transformer.describe())
    print(base_transformer.attack())
    print(base_transformer.transform())
    print(base_transformer.attack())
    print(base_transformer.revert())

    print("evolved:")
    evolved_transformer = transforming_factory.create_evolved()
    print(evolved_transformer.describe())
    print(evolved_transformer.attack())
    print(evolved_transformer.transform())
    print(evolved_transformer.attack())
    print(evolved_transformer.revert())


if __name__ == "__main__":
    main()

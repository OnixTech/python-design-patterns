from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def main() -> None:
    healing_factory = HealingCreatureFactory()

    print("Testing Creature with healing capability")

    print("base:")
    base_healer = healing_factory.create_base()
    healer = cast(HealCapability, base_healer)
    print(base_healer.describe())
    print(base_healer.attack())
    print(healer.heal())

    print("evolved:")
    evolved_healer = healing_factory.create_evolved()
    healer = cast(HealCapability, evolved_healer)
    print(evolved_healer.describe())
    print(evolved_healer.attack())
    print(healer.heal())

    transforming_factory = TransformCreatureFactory()

    print("Testing Creature with transform capability")

    print("base:")
    base_transformer = transforming_factory.create_base()
    transformer = cast(TransformCapability, base_transformer)
    print(base_transformer.describe())
    print(base_transformer.attack())
    print(transformer.transform())
    print(base_transformer.attack())
    print(transformer.revert())

    print("evolved:")
    evolved_transformer = transforming_factory.create_evolved()
    transformer = cast(TransformCapability, evolved_transformer)
    print(evolved_transformer.describe())
    print(evolved_transformer.attack())
    print(transformer.transform())
    print(evolved_transformer.attack())
    print(transformer.revert())


if __name__ == "__main__":
    main()

from ex0 import AquaFactory, FlameFactory
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)
from ex2.exceptions import InvalidStrategyError


def single_battle(
        opponents: list[tuple[CreatureFactury, BattleStrategy]]
        ) -> None:
    
    print(opponents)
    print("*** Tournament ***")

    if len(opponents) < 2:
        raise ValueError("At least two opponents are requiered")
        return

    try:
        for a in range(len(opponents)):
            for b in range(a + 1, len(opponents)):
                factory_a, strategy_a = opponents[a]
                factory_b, strategy_b = opponents[b]

                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()

                print("* Battle *")
                print(f"{creature_a.describe()}")
                print("vs.")
                print(f"{creature_b.describe()}")
                print("now fight!")

                actions_a = strategy_a.act(creature_a)

                for action in actions_a:
                    print(action)

                actions_b = strategy_b.act(creature_b)

                for action in actions_b:
                    print(action)

    except InvalidStrategyError as er:
        print(f"Battle error, aborting tournament: {er}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    tournament_0: list[Opponent] = [
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ]

    single_battle(tournament_0)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    tournament_1: list[Opponent] = [
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ]

    single_battle(tournament_1)

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), "
        "(Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )

    tournament_2: list[Opponent] = [
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ]

    single_battle(tournament_2)

if __name__ == "__main__":
    main()

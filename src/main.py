from collectors import DataCollector
from analyze import PatternAnalyzer
from generator import IdeaGenerator

def run():
    print("\nStarting system...\n")

    c = DataCollector()
    a = PatternAnalyzer()
    g = IdeaGenerator()

    # Step 1: Collect
    c.collect_youtube()
    c.collect_twitter()
    c.collect_news()

    # Step 2: Analyze
    insights = a.analyze()
    print("\nPatterns Found:\n")
    print(insights)

    # Step 3: Generate ideas
    ideas = g.generate(insights)
    print("\nGenerated Ideas:\n")
    print(ideas)


if __name__ == "__main__":
    run()

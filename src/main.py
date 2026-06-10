import sys
import argparse
import warnings
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from crew import research_crew

# Suppress non-critical warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', message='.*urllib3.*')
warnings.filterwarnings('ignore', message='.*RequestsDependencyWarning.*')

load_dotenv()

def run(topic: str, save_report: bool = True):
    """Run the research crew on a given topic.

    Args:
        topic: The research topic
        save_report: Whether to save the report to a file
    """
    if not topic or not topic.strip():
        print("❌ Error: Topic cannot be empty")
        return None

    topic = topic.strip()
    print(f"\n🔍 Starting research on: {topic}")
    print("=" * 60)

    try:
        result = research_crew.kickoff(inputs={"topic": topic})

        print("\n" + "=" * 60)
        print(f"✅ Research completed for: {topic}")
        print("=" * 60)
        print(result)
        print("=" * 60)

        if save_report and result:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"report_{topic.replace(' ', '_')}_{timestamp}.md"

            # Create reports directory if it doesn't exist
            reports_dir = Path(__file__).parent / "reports"
            reports_dir.mkdir(exist_ok=True)

            filepath = reports_dir / filename

            try:
                # Convert CrewOutput object to string
                result_str = str(result)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# Research Report: {topic}\n\n")
                    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write(result_str)

                print(f"\n📄 Report saved to: reports/{filename}")
            except Exception as save_error:
                print(f"\n⚠️  Warning: Could not save report to file: {str(save_error)}")

        return result

    except KeyboardInterrupt:
        print("\n\n⏸️  Research interrupted by user")
        return None
    except Exception as e:
        print(f"\n❌ Error during research: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Research Assistant - Gather, analyze, and report on any topic',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Examples:
  python main.py "Artificial Intelligence"
  python main.py "Climate Change" --no-save
  python main.py "Python Programming"
        '''
    )

    parser.add_argument(
        'topic',
        nargs='?',
        help='The topic to research'
    )

    parser.add_argument(
        '--no-save',
        action='store_true',
        help='Do not save the report to a file'
    )

    args = parser.parse_args()

    # Get topic from argument or prompt user
    topic = args.topic
    if not topic:
        print("\n🤖 Research Assistant")
        print("=" * 60)
        topic = input("Enter the topic you want to research: ").strip()

    if not topic:
        print("❌ No topic provided. Exiting.")
        sys.exit(1)

    run(topic, save_report=not args.no_save)

if __name__ == "__main__":
    main()
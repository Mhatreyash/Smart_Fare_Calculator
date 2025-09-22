from rich.console import Console
from rich.table import Table

def round_to_nearest_half(number):
  """Rounds a number to the nearest 0.5."""
  return round(number * 2) / 2

def calculate_fare(base_fare, cost_per_km, cost_per_minute, surge_multiplier, distance, time, minimum_fare):
  """Calculates the final taxi or rickshaw fare."""

  calculated_fare = base_fare + (distance * cost_per_km) + (time * cost_per_minute)
  surge_adjusted_fare = calculated_fare * surge_multiplier
  rounded_fare = round_to_nearest_half(surge_adjusted_fare)

  final_fare = max(rounded_fare, minimum_fare)

  return final_fare, base_fare, (distance * cost_per_km), (time * cost_per_minute), (surge_multiplier - 1) * calculated_fare if surge_multiplier > 1 else 0

def main():
  """Main function to run the Smart Fare Calculator."""

  console = Console()

  console.print("[bold cyan]SMART FARE CALCULATOR[/bold cyan]")

  try:
    base_fare = float(console.input("Enter the base fare (₹): "))
    cost_per_km = float(console.input("Enter the cost per km (₹): "))
    cost_per_minute = float(console.input("Enter the cost per minute (₹): "))
    surge_multiplier = float(console.input("Enter the surge multiplier (e.g., 1.0 for no surge): "))
    distance = float(console.input("Enter the distance of the ride in km: "))
    time = float(console.input("Enter the duration of the ride in minutes: "))
    minimum_fare = float(console.input("Enter the minimum fare (₹): "))

    final_fare, base, distance_cost, time_cost, surge_cost = calculate_fare(
        base_fare, cost_per_km, cost_per_minute, surge_multiplier, distance, time, minimum_fare
    )

    table = Table(title="Fare Breakdown")

    table.add_column("Component", justify="right", style="cyan", no_wrap=True)
    table.add_column("Amount (₹)", style="magenta")

    table.add_row("Base Fare", f"{base:.2f}")
    table.add_row("Distance Charge", f"{distance_cost:.2f}")
    table.add_row("Time Charge", f"{time_cost:.2f}")
    if surge_cost > 0:
        table.add_row("Surge Charge", f"{surge_cost:.2f}")
    table.add_row("[bold]Total Fare[/bold]", f"[bold]{final_fare:.2f}[/bold]")


    console.print(table)

  except ValueError:
    console.print("[bold red]Invalid input. Please enter numeric values.[/bold red]")


if __name__ == "__main__":
  main()

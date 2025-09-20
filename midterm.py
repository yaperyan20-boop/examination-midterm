def main():
    x, y = 0, 0
    print("Simple GPS tracker — start at (0, 0).")
    print("Enter N / S / E / W or full words (north, south, east, west). Type STOP to finish.\n")

    while True:
        try:
            cmd = input("Enter direction (N/S/E/W or STOP): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            # graceful exit if user presses Ctrl+C / Ctrl+D
            print("\nSession interrupted by user.")
            break

        if cmd == "stop":
            break

        if cmd in ("n", "north"):
            y += 1
            print(f"Moved North. Current position: ({x}, {y})")
        elif cmd in ("s", "south"):
            y -= 1
            print(f"Moved South. Current position: ({x}, {y})")
        elif cmd in ("e", "east"):
            x += 1
            print(f"Moved East. Current position: ({x}, {y})")
        elif cmd in ("w", "west"):
            x -= 1
            print(f"Moved West. Current position: ({x}, {y})")
        else:
            print("Invalid input. Please enter N/S/E/W or north/south/east/west, or STOP to end.")

    # Session ended — show final info
    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")
    if x == 0 and y == 0:
        print("You have returned to the origin (0, 0).")
    else:
        print("You did NOT return to the origin (0, 0).")

if _name_ == "_main_":
    main()

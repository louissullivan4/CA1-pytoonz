from pytoonz import Track, Pytoonz


def main():
    """Main method that contains our test block
    """
    pytoonz = Pytoonz()
    track1 = Track("Looking for me", "Paul Woolford and Diplo/Lomax")
    # print(track1)
    track2 = Track("Giants", "Dermot Kennedy")
    # print(track2)
    track3 = Track("Holy", "Justin Bieber Ft Chance")
    # print(track3)
    track4 = Track("Lemonade", "Internet Money / Gunna / Toliver")
    pytoonz.add_after(track1)
    pytoonz.add_track(track2)
    # pytoonz.add_track(track3)
    # print(pytoonz.length())
    # print(pytoonz.play())
    # print(pytoonz.get_current())
    # pytoonz.prev_track()
    # print(pytoonz.get_current())
    pytoonz.next_track()
    # pytoonz.next_track()
    # pytoonz.reset()
    # print(pytoonz.get_current())
    # pytoonz.prev_track()
    print(pytoonz.get_current())
    pytoonz.remove_current()
    print(pytoonz.get_current())
    # print(pytoonz)
    # pytoonz.add_track(track4)
    pytoonz.play()
    # pytoonz.next_track()
    print(pytoonz)

    # playlist = Pytoonz()
    # print(playlist)
    # playlist.play()
    # print(playlist.length())
    # print(playlist.get_current())
    # banger = Track("Kilby Girl", "Backseat Lovers", 0)
    # banger2 = Track("Didya think", "Arlie", 0)
    # banger3 = Track("Psychics", "Peach Pit", 0)
    # playlist.add_track(banger)
    # playlist.add_track(banger2)
    # playlist.add_track(banger3)
    # print(playlist.length())
    # print(playlist.get_current())
    # playlist.play()
    # playlist.next_track()
    # print(playlist.play())
    # playlist.next_track()
    # playlist.play()
    # playlist.reset()
    # print(playlist)
    # playlist.remove_current()
    # print(playlist)
    # playlist.add_after(banger)
    # print(playlist)


if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()

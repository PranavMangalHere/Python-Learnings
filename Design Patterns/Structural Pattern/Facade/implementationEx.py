class Projector:
    def on(self):
        print("Projector turned ON")

    def off(self):
        print("Projector turned OFF")


class SoundSystem:
    def on(self):
        print("Sound System ON")

    def off(self):
        print("Sound System OFF")


class Lights:
    def dim(self):
        print("Lights dimmed")

    def on(self):
        print("Lights turned ON")


class StreamingService:
    def play(self, movie):
        print(f"Playing movie: {movie}")


# ❌ Client Without Facade
# projector = Projector()
# sound = SoundSystem()
# lights = Lights()
# stream = StreamingService()

# projector.on()
# sound.on()
# lights.dim()
# stream.play("Inception")

## instead Apply facade pattern
class HomeTheaterFacade:
    def __init__(self):
        self.projector = Projector()
        self.sound = SoundSystem()
        self.lights = Lights()
        self.stream = StreamingService()

    def watch_movie(self, movie):
        print("\nStarting Movie Setup...")
        self.projector.on()
        self.sound.on()
        self.lights.dim()
        self.stream.play(movie)

    def end_movie(self):
        print("\nShutting Down...")
        self.projector.off()
        self.sound.off()
        self.lights.on()

## now client will call this using facade pattern
theater = HomeTheaterFacade()
theater.watch_movie("Inception")
theater.end_movie()
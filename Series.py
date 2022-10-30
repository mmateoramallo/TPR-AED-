class Serie:
    def __init__(self, poster_link, series_title, runtime_of_series, certificate, runtime_of_episodes, genre, IMDB_rating, Overwiew, No_of_Vote):
        self.poster_link = poster_link
        self.series_title = series_title
        self.runtime_of_series = runtime_of_series
        self.certificate = certificate
        self.runtime_of_episodes = runtime_of_episodes
        self.genre = genre
        self.iMDB_rating = IMDB_rating
        self.overwiew = Overwiew
        self.no_of_Vote = No_of_Vote

    def __str__(self):
        res = 'Link del Póster: ' + str(self.poster_link) + ' | ' + ' Título de la Serie: ' + \
              str(self.series_title) + ' | ' + ' Tiempo de Emisión: ' + str(self.runtime_of_series) \
              + ' | ' + ' Categoría: ' + str(self.certificate) + ' | ' + ' Tiempo Prom. de Capítulos: ' \
              + str(self.runtime_of_episodes) + ' | ' 'Género: ' + str(self.genre) + ' | ' \
              + ' Puntaje en IMDB: ' + str(self.iMDB_rating) + ' | ' + ' Resumen/Overview: ' \
              + str(self.overwiew) + ' | ' + ' Número de Votos: ' + str(self.no_of_Vote)
        return res

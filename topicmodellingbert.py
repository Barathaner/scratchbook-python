from bertopic import BERTopic

text = """Eine unvorhergesehene Gesellschaft
I
n einer Höhle in der Erde, da lebte ein Hobbit.
Nicht in einem schmutzigen, nassen Loch, in
das die Enden von irgendwelchen Würmern herabbaumelten und das nach Schlamm und Moder
roch. Auch nicht etwa in einer trockenen Kieshöhle, die so kahl war, dass man sich nicht einmal
niedersetzen oder gemütlich frühstücken konnte.
Es war eine Hobbithöhle, und das bedeutet Behaglichkeit.
Diese Höhle hatte eine kreisrunde Tür wie ein
Bullauge. Sie war grün gestrichen und in der Mitte
saß ein glänzend gelber Messingknopf. Die Tür
führte zu einer röhrenförmig langen Halle, zu einer Art Tunnel, einem Tunnel mit getäfelten Wänden. Der Boden war mit Fliesen und Teppichen
ausgelegt, es gab Stühle da von feinster Politur und
an den Wänden Haken in Massen für Hüte und
Mäntel, denn der Hobbit hatte Besucher sehr gern.
Der Tunnel wand und wand sich, führte aber nicht
tief ins Innere des Berges hinein, den alle Leute
viele Meilen weit rund im Lande schlechthin »den
Berg« nannten. Zahlreiche kleine, runde Türen
öffneten sich zu diesem Tunnel, zunächst auf der
einen Seite und dann auch auf der anderen.
Treppen zu steigen brauchte der Hobbit nichtSchlafräume, Badezimmer, Keller, Speisekammern
(eine Masse von Speisekammern), Kleiderschränke
(ganze Räume standen ausschließlich für die Unterbringung seiner Garderobe zur Verfügung), Küchen, Esszimmer – alles lag an demselben langen
Korridor. Die besten Zimmer lagen übrigens auf
der linken Seite (wenn man hineinkommt), denn
ausschließlich diese hatten Fenster, tief gesetzte,
runde Fenster, die hinaus auf den Garten blickten
und über die Wiesen, die sich gemächlich hinab bis
zum Fluss neigten.
Dieser Hobbit war ein sehr wohlhabender Hobbit und sein Name war Beutlin. Die Beutlins hatten
seit undenklichen Zeiten in der Nachbarschaft des
»Berges« gelebt und die Leute hielten sie für außerordentlich achtbar – nicht nur weil die meisten der
Beutlins reich, sondern weil sie noch nie in ein
Abenteuer verstrickt gewesen waren und nie etwas
Unvorhergesehenes getan hatten. Man konnte im
Voraus sagen, was ein Beutlin auf eine Frage antworten würde, ohne dass man sich die Mühe machen musste, diese Frage wirklich zu stellen. Dies
hier aber ist eine Geschichte von einem Beutlin,
der trotzdem Abenteuer erlebte und sich selbst
über völlig unvorhergesehene Fragen reden hörte.
Vielleicht verlor er bei seinen Nachbarn an Ansehen, aber er gewann – nun, ihr werdet ja sehen, ob
er am Ende überhaupt etwas gewann.
Die Mutter unseres Hobbits – was ist eigentlich
ein Hobbit? Ich glaube, dass die Hobbits heutzu-tage einer Beschreibung bedürfen, da sie selten geworden sind und scheu vor den »Großen Leuten«,
wie sie uns zu nennen pflegen. Sie sind (oder waren) ungefähr halb so groß wie wir und kleiner als
die bärtigen Zwerge (sie tragen jedoch keine
Bärte). Es ist wenig, sozusagen gar nichts von Zauberei an ihnen, ausgenommen die alltägliche Gabe,
rasch und lautlos zu verschwinden, wenn großes
dummes Volk wie du und ich angetapst kommt und
Radau macht wie Elefanten, was sie übrigens eine
Meile weit hören können. Sie neigen dazu, ein bisschen fett in der Magengegend zu werden. Sie kleiden sich in leuchtende Farben (hauptsächlich in
Grün und Gelb). Schuhe kennen sie überhaupt
nicht, denn an ihren Füßen wachsen natürliche, lederartige Sohlen und dickes, warmes, braunes
Haar, ganz ähnlich wie das Zeug auf ihrem Kopf
(das übrigens kraus ist). Die Hobbits haben lange,
geschickte, braune Finger, gutmütige Gesichter
und sie lachen ein tiefes, saftiges Lachen (besonders nach den Mahlzeiten; Mittagessen halten sie
zweimal am Tag, wenn sie es bekommen können).
Nun, das sei vorerst genug und wir wollen fortfahren.
Bilbo Beutlin hieß unser Hobbit und seine Mutter war die berühmte Belladonna Tuk, eine der
drei ausgezeichneten Töchter des alten Tuk. Der
alte Tuk war das Haupt der Hobbits, die jenseits des
»Wassers« wohnten, des schmalen Flusses am Fuß
des Berges. Es wurde oft gemunkelt, dass vor langerZeit einmal ein Tuk eine Fee geheiratet habe. Das
war natürlich Unsinn. Aber sicherlich war bei ihnen nicht alles hobbitmäßig. Denn ab und zu ging
ein Angehöriger der Tuks fort und stürzte sich in
Abenteuer. Sie verschwanden heimlich und die Familie vertuschte es. Tatsache ist jedenfalls, dass die
Tuks nicht ganz so geachtet waren wie die Beutlins,
obgleich sie unzweifelhaft reicher waren.
Nicht, dass Belladonna Tuk jemals in irgendwelche Abenteuer verwickelt gewesen wäre, nachdem
sie die Frau von Mister Bungo Beutlin geworden
war. Bungo, Bilbos Vater, baute (teilweise mit ihrem
Geld) für sie die kostspieligste Hobbithöhle, die jemals unterhalb oder oberhalb des Berges oder jenseits des Wassers gebaut worden war. Und dort lebten sie bis an das Ende ihrer Tage. Indessen ist es
wahrscheinlich, dass Bilbo, ihr einziger Sohn, obgleich er doch aussah und sich genauso benahm
wie eine zweite Ausgabe seines grundsoliden und
behäbigen Vaters, irgendetwas Wunderliches in seinen Anlagen von der Tukseite übernommen hatte.
Es war etwas, das nur auf die Chance wartete, um
ans Licht zu kommen. Die Chance ergab sich erst,
als Bilbo Beutlin etwa fünfzig Jahre alt geworden
war, in der wunderschönen Hobbithöhle wohnte,
die sein Vater erbaut hatte, und sich augenscheinlich zur Ruhe gesetzt hatte.
Eines Morgens, vor langer Zeit, in der großen
Stille, als es noch wenig Geräusche und mehr Grün
gab, als die Hobbits noch zahlreich und glücklich"""


import nltk
import spacy
from nltk.stem.snowball import SnowballStemmer

# Initialisierung
nltk.download('stopwords')
nltk.download('punkt')
stemmer = SnowballStemmer(language='german')
nlp = spacy.load("de_core_news_sm")
stopwords = set(nltk.corpus.stopwords.words('german'))

# Funktionen
def tokenize(text):
    return nltk.word_tokenize(text, language='german')

def remove_stopwords(tokens):
    return [token for token in tokens if token.lower() not in stopwords]

def lemmatize(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

def stem(tokens):
    return [stemmer.stem(token) for token in tokens]

# Text
tokens = tokenize(text)
print(f"Tokens: {tokens}")

tokens_no_stopwords = remove_stopwords(tokens)
print(f"Tokens ohne Stopfwörter: {tokens_no_stopwords}")

lemmatized_tokens = lemmatize(tokens_no_stopwords)
print(f"Lemmatized Tokens: {lemmatized_tokens}")

stemmed_tokens = stem(lemmatized_tokens)
print(f"Stemmed Tokens: {stemmed_tokens}")

topic_model = BERTopic(language="german", calculate_probabilities=True)
topics, probs = topic_model.fit_transform(text.split("\n"))

# Die ermittelten Topics anzeigen
out = topic_model.get_topic_info()
print(out)
with open('bertopic_output.txt', 'w', encoding='utf-8') as file:
    file.write(str(out))
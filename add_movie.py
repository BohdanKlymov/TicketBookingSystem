from app import app, db
from app.models import Movies
from PIL import Image

with app.app_context():
    db.create_all()

    movie_Inception = Movies(
        title =  "Inception",
        price = 12,
        movie_description = "A master thief named Dom Cobb specializes in stealing secrets from people’s subconscious minds during dreams. When offered a chance to have his criminal record erased, he takes on a nearly impossible task — not to steal an idea, but to plant one deep within a target’s mind. As Cobb’s team delves through layers of dreams within dreams, the boundaries between reality and imagination blur, testing their sanity and sense of time.",
        movie_yearOfRelease = "2010",
        movie_picture = "\\inception.jpg"
    )
    movie_TheShawshankRedemption = Movies(
        title = "The Shawshank Redemption",
        price = 10,
        movie_description = "Andy Dufresne, a quiet banker wrongfully convicted of murdering his wife, is sentenced to life at Shawshank Prison. Over decades, he forms a deep friendship with fellow inmate Red and gradually earns respect by helping the warden with financial schemes. Beneath the monotony of prison life, Andy secretly plans a daring escape — one that becomes a profound symbol of hope and human resilience.",
        movie_yearOfRelease = "1994",
        movie_picture = "\\shawshankRedemption.jpg"
    )
    movie_TheDarkKnight = Movies(
        title = "The Dark Knight",
        price = 13,
        movie_description = "Batman faces chaos incarnate in the form of the Joker, a sadistic criminal mastermind determined to prove that even the noblest people can be corrupted. As Gotham City descends into anarchy, Batman must question his moral code and the line between hero and vigilante. With stunning action, psychological tension, and unforgettable performances, this film redefined the superhero genre.",
        movie_yearOfRelease = "2008",
        movie_picture = "\\TheDarkKnight.jpg"
    )
    movie_Titanic = Movies(
        title = "Titanic",
        price = 11,
        movie_description = "A young artist, Jack Dawson, wins a ticket aboard the RMS Titanic, the most luxurious ship ever built. Onboard, he meets Rose DeWitt Bukater, a wealthy young woman trapped in a loveless engagement. Their forbidden romance blossoms against the backdrop of the doomed voyage, culminating in tragedy as the ship meets its fateful iceberg. A sweeping epic of love, loss, and survival.",
        movie_yearOfRelease = "1997",
        movie_picture = "\\titanic.jpg"
    )
    movie_ForrestGump = Movies(
        title = "Forrest Gump",
        price = 9,
        movie_description = "Forrest Gump, a kind-hearted man with a low IQ, unwittingly influences key moments in American history — from the Vietnam War to the rise of Apple Computers. Despite his simplicity, Forrest lives a life of remarkable adventure, driven by love for his childhood friend Jenny. His story is a touching exploration of innocence, destiny, and perseverance.",
        movie_yearOfRelease = "1994",
        movie_picture = "\\ForrestGump.jpg"
    )
    movie_TheMatrix = Movies(
        title = "The Matrix",
        price = 12,
        movie_description = "Computer hacker Neo discovers that the reality he knows is actually a simulation created by intelligent machines to enslave humanity. Recruited by the mysterious Morpheus, Neo must learn to control the digital world and fulfill his destiny as 'The One.' With groundbreaking visual effects and philosophical depth, The Matrix revolutionized sci-fi and action cinema, exploring freedom, perception, and identity.",
        movie_yearOfRelease = "1999",
        movie_picture = "\\Matrix.jpg"
    )
    movie_Gladiator = Movies(
        title = "Gladiator",
        price = 10,
        movie_description = "Roman general Maximus Decimus Meridius is betrayed when the corrupt prince Commodus murders his father and seizes the throne. Enslaved and forced to fight as a gladiator, Maximus rises through the ranks of the arena to confront the man who destroyed his family. Filled with epic battles, powerful emotion, and moral complexity, it’s a story of honor, revenge, and redemption.",
        movie_yearOfRelease = "2000",
        movie_picture = "\\gladiator.jpg"
    )
    movie_Godfather = Movies(
        title = "The Godfather",
        price = 14,
        movie_description = "The Corleone family rules New York’s criminal underworld with ruthless efficiency and quiet dignity. When patriarch Vito Corleone is nearly assassinated, his reluctant son Michael is drawn into the family business, transforming from war hero to cold-blooded mafia boss. A masterpiece of storytelling, The Godfather examines power, loyalty, and the corruption of the American dream.",
        movie_yearOfRelease = "1972",
        movie_picture = "\\TheGodfather.jpg"
    )
    movie_JurassicPark = Movies(
        title = "Jurassic Park",
        price = 11,
        movie_description = "Visionary billionaire John Hammond creates a theme park filled with living dinosaurs cloned from ancient DNA. But when the park’s security systems fail, visitors must fight to survive as the prehistoric creatures reclaim their dominance. Blending cutting-edge special effects with thrilling storytelling, Jurassic Park is a landmark in cinematic spectacle and scientific hubris.",
        movie_yearOfRelease = "1993",
        movie_picture = "\\JurassicWorld.jpg"
    )
    movie_Parasite = Movies(
        title = "Parasite",
        price = 13,
        movie_description = "A struggling Korean family cleverly infiltrates the household of a wealthy couple by posing as unrelated, qualified professionals. What begins as a smart con spirals into a darkly humorous and tragic confrontation between social classes. Parasite masterfully weaves suspense, satire, and symbolism into a biting critique of economic inequality and human greed.",
        movie_yearOfRelease = "2019",
        movie_picture = "\\parasite.jpg"
    )
    db.session.add_all([
    movie_Inception, 
    movie_TheShawshankRedemption,
    movie_TheDarkKnight, 
    movie_Titanic,
    movie_ForrestGump, 
    movie_TheMatrix,
    movie_Gladiator, 
    movie_Godfather,
    movie_JurassicPark, 
    movie_Parasite
])
    db.session.commit()
    print("✅ Movie added successfully!")

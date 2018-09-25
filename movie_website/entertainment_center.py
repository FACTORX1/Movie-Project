import fresh_tomatoes
import media
#9 instances of my favourite movie
push=media.Movie("Push",
				 "http://mysoundtrack.ru/wp-content/uploads/2010/06/Push-soundtrack.jpg",
				 "https://www.youtube.com/watch?v=Pl3KNqCEtQ4",
				 "Two young Americans with special abilities must race to find a girl in Hong Kong before a shadowy government organization called Division does.",
				 "https://meetthebookmistress.files.wordpress.com/2017/03/c17c1-five2bstars.png")
Knowing=media.Movie("Knowing",
					"https://images-na.ssl-images-amazon.com/images/I/61ysUoPkztL._AC_UL320_SR254,320_.jpg",
					"https://www.youtube.com/watch?v=RQE-rB3Nkh8",
					"M.I.T. professor John Koestler links a mysterious list of numbers from a time capsule to past and future disasters and sets out to prevent the ultimate catastrophe.",
					"http://www.peterspartyservice.com/wp-content/uploads/Recensies.png")
Law_abiding_citizen=media.Movie("Law abiding citizen",
								"http://www.heyuguys.com/images/Law-Abiding-Citizen-Poster.jpg",
								"https://www.youtube.com/watch?v=LX6kVRsdXW4",
								"A frustrated man decides to take justice into his own hands after a plea bargain sets one of his family's killers free. He targets not only the killer but also the district attorney and others involved in the deal.",
								"https://weekly.blog.gustavus.edu/files/2012/11/STAR-3.5-2.png")
High_school_musical=media.Movie("High School Musical 4",
								"https://www.exploretalent.com/articles/wp-content/uploads/2016/03/ET-Blog-HS-Musical-4.png",
								"https://www.youtube.com/watch?v=JO_Oir72EDs",
								"The fourth installment of the Disney musical franchise, High School Musical",
								"http://www.frenchcollection.com.au/site/wp-content/uploads/3-5_StarRating-3.png")
world_war_z=media.Movie("World War Z",
						"http://www.impawards.com/2013/posters/world_war_z_ver2_xlg.jpg",
						"https://www.youtube.com/watch?v=Md6Dvxdr0AQ",
						"Former United Nations employee Gerry Lane traverses the world in a race against time to stop the Zombie pandemic that is toppling armies and governments, and threatening to destroy humanity itself.",
						"http://4.bp.blogspot.com/-7j95ujkNsJA/UdkCe2a7g7I/AAAAAAAAARs/j67uCEDKIgI/s1600/4stars1.jpg")
The_mask=media.Movie("The Mask",
					"https://upload.wikimedia.org/wikipedia/en/4/4b/The_Mask_%28film%29_poster.jpg",
					"https://www.youtube.com/watch?v=hOqVRwGVUkA",
					"Bank clerk Stanley Ipkiss is transformed into a manic superhero when he wears a mysterious mask.",
					"http://www.northeastrehab.com/wp-content/uploads/2017/03/4_5_StarRating.png")

movies = [push,The_mask,world_war_z,Knowing,Law_abiding_citizen,High_school_musical]

# Create and open the movie website .html file
fresh_tomatoes.open_movies_page(movies)							

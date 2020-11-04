class Data:

    def __init__(self, title, heading, desc, link1, link2):
        super().__init__()
        self.title = title
        self.heading = heading
        self.desc = desc
        self.link1 = link1
        self.link2 = link2
        


data1 = Data('Project1',
             'Digit Recognizer',
             'Digit Recognizer using Artificial Neural Network. I have used Neural Network with 3 hidden layers. Data is used from kaggle to train the model. ',
             'https://adityamorankar-digitrecognizer.herokuapp.com/',
             'https://github.com/adi112100/django_digitrecognizer'
             
             )

data2 = Data('Project2',
             'Diabetes Prediction',
             'Diabetes Prediction model using Random Forest Classifier. I have used sklearn library along with pandas and numpy to train dataset.',
             'https://adityamorankar-predictdiabetes.herokuapp.com/',
             'https://github.com/adi112100/django_predictdiabetes'
             
             )

data3 = Data('Project3',
             'Personalize news app',
             'Personalize news app which provide you recommended news feed which you will find intresting and useful.',
             'https://adityamorankar-dailynews.herokuapp.com/',
             '/error/'
             
             )

data4 = Data('Project4',
             'Smart Attendance app',
             'Attendance app based on facial recognition using deep learning and django as a backend',
             'https://adityamorankar-smartattendance.herokuapp.com/',
             'https://github.com/adi112100/smart-attendance-app'
             
             )

data5 = Data('Project5',
             'Path Finding Visualizer',
             'It finds the path from point A to point B. you can choose diffrent algorithms (both weighted and unweighted) and can create barriers(walls)',
             'https://pathfinderbyaditya.netlify.app/',
             'https://github.com/adi112100/PathFindier_backend',
             )


lst = [data1, data2, data3, data4, data5]

class Links:

    def __init__(self, link, title, image):
        super().__init__()
        self.link = link
        self.title = title
        self.image = image


lnk1 = Links('game1/', 'roll ball', 'roll.jpg')
lnk2 = Links('https://myfirstwebgame.000webhostapp.com/alpha%20Battle/index.html', 'alpha battle' ,'keyboard.jpg')
lnk3 = Links('https://myfirstwebgame.000webhostapp.com/sort_visualizer/index.html', 'sort_visualizer simulation' ,'sort.png')
lnk4 = Links('game2/', 'Solar System', 'solar.jpg')
lnk5 = Links('game3/', 'Box Shooter', 'shoot.jpg')


gamelinks = [lnk1, lnk2, lnk3, lnk4, lnk5]
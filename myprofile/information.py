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


lst = [data1, data2]



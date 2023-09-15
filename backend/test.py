from API import get_prediction

# path to trained model
model_path = "model.h5"

# malicious examples
# http://ww1.edurenewal.com/
# https://delta-miners.com/

url = "https://onlinesbi.digital/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)
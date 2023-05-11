# Arvigo Big Five Personality ML Model

> This ML model would come in hand in analyzing personalities given a spectrum of questions.

## Development

### Dependencies

```
Flask==2.3.2
joblib==1.2.0
matplotlib==3.7.1
numpy==1.23.0
pandas==2.0.1
protobuf==4.23.0
scikit_learn==1.2.2
yellowbrick==1.5
```

### How to run

```
flask --app aleksandro run
```

### How to run with live reload

```
flask --app aleksandro --debug run
```


## Usage

#### Endpoint for actual usage

```
URL: 127.0.0.1:5000/detect_personality
Method: POST
Body: JSON
```

In HTTPie, we can write this as: 

```
http POST http://127.0.0.1:5000/detect_personality \
    Content-Type:application/json \
    EXT1:=4 EXT2:=4 EXT3:=4 EXT4:=4 EXT5:=4 \
    EXT6:=4 EXT7:=4 EXT8:=4 EXT9:=4 EXT10:=4 \
    EST1:=4 EST2:=4 EST3:=4 EST4:=4 EST5:=4 \
    EST6:=4 EST7:=4 EST8:=4 EST9:=4 EST10:=4 \
    AGR1:=4 AGR2:=4 AGR3:=4 AGR4:=4 AGR5:=4 \
    AGR6:=4 AGR7:=4 AGR8:=4 AGR9:=4 AGR10:=4 \
    CSN1:=4 CSN2:=4 CSN3:=4 CSN4:=4 CSN5:=4 \
    CSN6:=4 CSN7:=4 CSN8:=4 CSN9:=4 CSN10:=4 \
    OPN1:=4 OPN2:=4 OPN3:=4 OPN4:=4 OPN5:=4 \
    OPN6:=4 OPN7:=4 OPN8:=4 OPN9:=4 OPN10:=4
```

It will return:

```
{
    "predicted_personality": [
        "Extraversion"
    ]
}
```

#### Endpoint for crosschecking result

```
URL: 127.0.0.1:5000/dummy_detect_personality
Method: POST
Body: JSON
```

In HTTPie, we can write this as: 

```
http POST http://127.0.0.1:5000/dummy_detect_personality \
    Content-Type:application/json
```

It _could_ return:

```
{
    "input": {
        "AGR1": 1,
        "AGR10": 1,
        "AGR2": 1,
        "AGR3": 4,
        "AGR4": 3,
        "AGR5": 4,
        "AGR6": 4,
        "AGR7": 3,
        "AGR8": 4,
        "AGR9": 1,
        "CSN1": 3,
        "CSN10": 4,
        "CSN2": 2,
        "CSN3": 2,
        "CSN4": 5,
        "CSN5": 2,
        "CSN6": 1,
        "CSN7": 3,
        "CSN8": 3,
        "CSN9": 5,
        "EST1": 4,
        "EST10": 5,
        "EST2": 2,
        "EST3": 4,
        "EST4": 5,
        "EST5": 4,
        "EST6": 3,
        "EST7": 4,
        "EST8": 5,
        "EST9": 1,
        "EXT1": 4,
        "EXT10": 4,
        "EXT2": 3,
        "EXT3": 1,
        "EXT4": 5,
        "EXT5": 3,
        "EXT6": 5,
        "EXT7": 1,
        "EXT8": 2,
        "EXT9": 4,
        "OPN1": 2,
        "OPN10": 5,
        "OPN2": 5,
        "OPN3": 5,
        "OPN4": 4,
        "OPN5": 4,
        "OPN6": 5,
        "OPN7": 1,
        "OPN8": 4,
        "OPN9": 4
    },
    "predicted_personality": [
        "Agreeableness"
    ]
}

```
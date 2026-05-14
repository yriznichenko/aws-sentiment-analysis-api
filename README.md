# aws-sentiment-analysis-api
Projekt AWS API


Ten projekt jest opartym na chmurze API analizy nastrojów zbudowanym z usług AWS.
API odbiera tekst w formacie JSON i zwraca:
- positive
- negative
- neutral

Używane usługi AWS:
- AWS Lambda
- Amazon API Gateway
- Amazon S3

Zbiór danych jest przechowywany w Amazon S3, a także zawarty w repozytorium jako: "sentiment_dataset.csv".

Przykład API
Request:
{
  "text": "This product is amazing"
}
=>:
{
  "text": "This product is amazing",
  "sentiment": "positive",
  "confidence": 1
}

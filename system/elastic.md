## Simple search

```json
GET /megacorp/employee/_search
{
    "query" : {
        "match" : {
            "last_name" : "Smith"
        }
    }
}
```

## More complicated search

```json
GET /megacorp/employee/_search
{
    "query" : {
        "bool": {
            "must": [
                "match" : {
                    "last_name" : "smith"
                }
            ],
            "filter": {
                "range" : {
                    "age" : { "gt" : 30 }
                }
            }
        }
    }
}
```

## Phrase search

Match exact sequences of words or phrases.

```json
GET /megacorp/employee/_search
{
    "query" : {
        "match_phrase" : {
            "about" : "rock climbing"
        }
    }
}
```

## Highlighting our searches

```json
GET /megacorp/employee/_search
{
    "query" : {
        "match_phrase" : {
            "about" : "rock climbing"
        }
    },
    "highlight": {
        "fields" : {
            "about" : {}
        }
    }
}
```

## Pagination

```
GET /_search?size=5
GET /_search?size=5&from=5
GET /_search?size=5&from=10
```

## Built-in analyzers

```
"Set the shape to semi-transparent by calling set_trans(5)"
```

### Standard analyzer

The standard analyzer is the default analyzer that Elasticsearch uses. It is the best general choice for analyzing text that may be in any language. It splits the text on word boundaries, as defined by the Unicode Consortium, and removes most punctuation. Finally, it lowercases all terms. It would produce

`set, the, shape, to, semi, transparent, by, calling, set_trans, 5`

### Simple analyzer
The simple analyzer splits the text on anything that isn’t a letter, and lowercases the terms. It would produce

`set, the, shape, to, semi, transparent, by, calling, set, trans`

### Whitespace analyzer
The whitespace analyzer splits the text on whitespace. It doesn’t lowercase. It would produce

`Set, the, shape, to, semi-transparent, by, calling, set_trans(5)``

### Language analyzers

Language-specific analyzers are available for many languages. They are able to take the peculiarities of the specified language into account. For instance, the english analyzer comes with a set of English stopwords (common words like and or the that don’t have much impact on relevance), which it removes. This analyzer also is able to stem English words because it understands the rules of English grammar.

The english analyzer would produce the following:

`set, shape, semi, transpar, call, set_tran, 5`

Note how transparent, calling, and set_trans have been stemmed to their root form.

## Mapping

JSON type                                   Field type
Boolean: true or false                      boolean
Whole number: 123                           long
Floating point: 123.45                      double
String, valid date: 2014-09-15              date
String: foo bar                             string

```
GET /gb/_mapping/tweet
``

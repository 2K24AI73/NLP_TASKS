<h2>Bag of Words & Cosine Similarity – Analysis</h2>

<h3>1. Word Order and Sentiment Analysis</h3>

<p>
The sentences <strong>"dog bites man"</strong> and
<strong>"man bites dog"</strong> have the exact same Bag of Words
representation because Bag of Words only counts how many times each word
appears. It does not consider the order of the words.
</p>

<table>
  <tr>
    <th>Word</th>
    <th>"dog bites man"</th>
    <th>"man bites dog"</th>
  </tr>
  <tr>
    <td>dog</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>bites</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>man</td>
    <td>1</td>
    <td>1</td>
  </tr>
</table>

<p>
Therefore, both sentences produce the same vector:
<strong>[1, 1, 1]</strong>.
</p>

<p>
<strong>Impact on sentiment analysis:</strong>
Bag of Words can lose important information about word order and context.
For sentiment analysis, this can cause problems when the meaning changes
because of the arrangement of words. More advanced approaches such as
<strong>n-grams, word embeddings, and Transformer models</strong> can
capture more contextual information.
</p>

<hr>

<h3>2. Sparsity Issues with a 100,000-Word Vocabulary</h3>

<p>
If the corpus contains <strong>100,000 unique vocabulary words</strong>,
each document is represented using a vector with up to 100,000 features.
Most documents will contain only a small fraction of those words.
</p>

<p>
For example, if a document contains only 100 words, approximately
<strong>99,900 positions</strong> in its Bag of Words vector will contain
zero.
</p>

<p>
This creates a <strong>sparse matrix</strong>.
If a dense NumPy matrix is used, a large amount of memory is wasted storing
zeros.
</p>

<table>
  <tr>
    <th>Vocabulary</th>
    <th>Features per Document</th>
    <th>Typical Result</th>
  </tr>
  <tr>
    <td>100 words</td>
    <td>100</td>
    <td>Small matrix</td>
  </tr>
  <tr>
    <td>10,000 words</td>
    <td>10,000</td>
    <td>Larger and sparse</td>
  </tr>
  <tr>
    <td>100,000 words</td>
    <td>100,000</td>
    <td>Very large and highly sparse</td>
  </tr>
</table>

<p>
The <strong>density decreases</strong> as the vocabulary becomes larger
because the number of zero entries increases. In practical NLP applications,
<strong>sparse matrix representations</strong> such as the ones provided by
Scikit-learn are preferred because they store mainly the non-zero values.
</p>

<hr>

<h3>3. Why Is the Cosine Similarity 0.0000?</h3>

<p>
Suppose the query is:
</p>

<blockquote>
  "machine learning algorithms for data"
</blockquote>

<p>
If <strong>Document 3</strong> receives a cosine similarity score of
<strong>0.0000</strong>, it means that the Bag of Words representation of
Document 3 has <strong>no words in common with the query</strong>.
</p>

<p>
For example:
</p>

<table>
  <tr>
    <th>Query</th>
    <th>Document 3</th>
  </tr>
  <tr>
    <td>machine</td>
    <td>football</td>
  </tr>
  <tr>
    <td>learning</td>
    <td>team</td>
  </tr>
  <tr>
    <td>algorithms</td>
    <td>match</td>
  </tr>
  <tr>
    <td>data</td>
    <td>player</td>
  </tr>
</table>

<p>
Because there are no overlapping words, the dot product between the two
Bag of Words vectors is zero. Therefore, their cosine similarity is:
</p>

<p align="center">
  <strong>Cosine Similarity = 0.0000</strong>
</p>

<p>
This does not necessarily mean that the documents have completely unrelated
meaning. It only means that <strong>Bag of Words could not detect a shared
word</strong>. For example, the words "machine" and "computer" may be
semantically related, but basic Bag of Words treats them as completely
different features.
</p>

<hr>

<h3>Conclusion</h3>

<ul>
  <li><strong>Bag of Words ignores word order.</strong></li>
  <li><strong>Large vocabularies create highly sparse matrices.</strong></li>
  <li><strong>Cosine similarity can be 0 when documents have no shared words.</strong></li>
  <li><strong>Bag of Words captures word frequency but not deeper semantic meaning.</strong></li>
  <li><strong>TF-IDF, word embeddings, and Transformer-based models can address some of these limitations.</strong></li>
</ul>

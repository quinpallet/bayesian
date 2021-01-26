# bayesian

Bayesian Filter: A filter that can be applied to automatic text classification using an algorithm called Naive Bayes.

## Requirements

- [Neologism dictionary for MeCab](https://github.com/neologd/mecab-ipadic-neologd)

## Prerequisites

- Python >= 3.7

## Usage

- NativeBayes.py

  - NativeBayes.fit(text, category) : Fit Native Bayes classifier according to text, category.
  - NativeBayes.predict(text) : Perform classification on an array of test vectors text.

- Sample

``` python
from nbayes import NaiveBayes

nb = NaiveBayes()

nb.fit('Python（パイソン）はインタープリタ型の高水準汎用プログラミング言語である。グイド・ヴァン・ロッサムにより創り出され、1991年に最初にリリースされたPythonの設計哲学は、有意なホワイトスペース(オフサイドルール)の顕著な使用によってコードの可読性を重視している。その言語構成とオブジェクト指向のアプローチは、プログラマが小規模なプロジェクトから大規模なプロジェクトまで、明確で論理的なコードを書くのを支援することを目的としている。', 'Python')
nb.fit('Pythonは動的に型付けされていて、ガベージコレクションされている。構造化（特に手続き型）、オブジェクト指向、関数型プログラミングを含む複数のプログラミングパラダイムをサポートしている。Pythonは、その包括的な標準ライブラリのため、しばしば「バッテリーを含む」言語と表現される。', 'Python')
nb.fit('Pythonは1980年代後半にABC言語の後継として考案された。2000年にリリースされたPython 2.0では、リスト内包表記や参照カウントによるガベージコレクションシステムなどの機能が導入された。', 'Python')
nb.fit('Java（ジャヴァ）は、汎用プログラミング言語とソフトウェアプラットフォームの双方を指している総称ブランドである。オラクル社 (Oracle Inc.) およびその関連会社の登録商標である。1996年にサン・マイクロシステムズ (Sun)社によって市場リリースされ、2010年に同社がオラクル社に吸収合併された事により、Javaの版権もそちらに移行した。', 'Java')
nb.fit('プログラミング言語Javaは、C++に類似の構文、クラスベースのオブジェクト指向、マルチスレッド、ガーベジコレクション、コンポーネント指向、分散コンピューティングといった特徴を持ち、平易性重視のプログラム書式による堅牢性と、仮想マシン上での実行によるセキュリティ性およびプラットフォーム非依存性が理念とされている。Javaプラットフォームは、Javaプログラムの実行環境または、実行環境と開発環境の双方を統合したソフトウェアであり、ビジネスサーバ、モバイル機器、組み込みシステム、スマートカードといった様々なハードウェア環境に対応したソフトウェア形態で提供されている。その中枢技術であるJava仮想マシンは各プラットフォーム環境間の違いを吸収しながら、Javaプログラムの適切な共通動作を実現する機能を備えている。このテクノロジは「write once, run anywhere」と標榜されていた。', 'Java')
nb.fit('JavaScript（ジャバスクリプト）とは、プログラミング言語のひとつである。JavaScriptはプロトタイプベースのオブジェクト指向スクリプト言語であるが、クラスなどのクラスベースに見られる機能も取り込んでいる。', 'JavaScript')
nb.fit('利用される場面はWebサイト・Webアプリ・バックエンド・デスクトップアプリ・モバイルアプリなど、ブラウザからサーバ、デスクトップからスマートフォンまで多岐にわたっている。', 'JavaScript')
nb.fit('Goはプログラミング言語の1つである。2009年、GoogleでRobert Griesemer、ロブ・パイク、ケン・トンプソンによって設計された。Goは、静的型付け、C言語の伝統に則ったコンパイル言語、メモリ安全性、ガベージコレクション、構造的型付け（英語版）、CSPスタイルの並行性などの特徴を持つ。Goのコンパイラ、ツール、およびソースコードは、すべてフリーかつオープンソースである。', 'Go')
nb.fit('軽量スレッディングのための機能、Pythonのような動的型付け言語のようなプログラミングの容易性、などの特徴もある。Go処理系としてはコンパイラのみが開発されている。マスコット・キャラクターはGopher（ホリネズミ）。', 'Go')

pre, scorelist = nb.predict('ケン・トンプソンが設計したプログラミング言語')
print(pre, scorelist)
```
```sh
Go [('Python', -25.38328973256337), ('Java', -27.792320251967077), ('JavaScript', -26.56550806818653), ('Go', -24.222876706717866)]
```

## License

&copy; 2021 [Ken Kurosaki](https://github.com/quinpallet).<br>
This project is [MIT](https://github.com/quinpallet/line_echo_bot/blob/master/LICENSE) licensed.

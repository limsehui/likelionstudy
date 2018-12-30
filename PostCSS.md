# PostCSS / CSSNext / CSS4

### 3.0 Installing Parcel

parcel: 일종의 module bundler. 즉 프로그램이나 소프트웨어를 만들 때 코드를 작성하면 코드가 여러 부분으로 나뉘어지는데 이 코드를 압축, 변환, 사용자 화 시켜주는 것이다.

```터
 npm install -g parcel -bundler
```

터미널에 위의 코드를 적어주면 install된다. 

package.jsond을 열어서 script를 작성한다.

```json
"scripts":{
    "start":"parcel index.html"
}
```

코드를 작성한 후 터미널에 밑으 명령을 적어주면 된다.

```
npm run start
```

위의 script를 실행시키는 것이다. 

실행시키고 나면 server running at "주소" 가 뜨는데 이 주소를 복사하여 브라우저에 넣으면 수정할 때 마다 파일을 열어 실행시키지 않아도 자동으로 로딩이 된다는 것이다.  (서버사용) 





### 3.1 PostCSS and Parcel

PostCSS: CSS조금 더 현대적으로 바꿔준다. 

```
npm install postcss-preset-env
```

터미널에 위의 명령어를 적으면 install된다.

그다음 package.json으로 들어가서 dependencies란에 적혀있는 것을 확인 할 수 있는데 이것으로는 부족하다. 

추가설정을 위해 ,를 찍고 새로운 아이템인 postcss를 만든다.

```json
"postcss":{
    "plugins":{
        "postcss-preset-env":{
            "stages":0
        }
    }
}
```

postcss-preset-env는 얼마나 젊은지 혹은 오래된 property를 사용할건지 정할 수 있다. 

stage 0은 아직 개발되지는 않았지만 곧 만들어질 예정을 이야기하는 것이다. 





### 3.2 Functional pseudo-classes

 maches: 많은 selectoers와 conditions들을 그룹화하여 적용할 수 있도록 해준다. 

```css
li:matches(:nth-child(even), .target){
    background-color: blue;
}
```

이것을 functional peseudo selector이라고 불리운다. 그 이유는 function처럼 작용하기 때문이다.

위의 코드는 짝수에만 배경색을 blue로 적용하겠다는 의미이다. 

```html
<li class="target"><a href="#" target="_blank">Link</a><li>
```

html에서 3번째 class에 target을 써 넣으면 짝수가 아니더라도 배경에 색이 입혀진다.

```css
li:not(.target){
    background-color:blue;
}
```

target을 제외한 class에 파란색배경이 입혀지는 것이다.





### 3.3 CSS Variables

css varoable : css가 프로그래밍언어처럼 보이게 해준다. 또한 글씨크기, 글씨체, 글씨색상 등을 저장 할 수 있게해준다.

```css
:root{
    --awesomeColor: red;
}
li: first-child a{
    color: var(--awesomeColor);
}
```

variabel을 추가하려면 root에 저장하면 되는데 root는 html문서 자체보다 더 높은 element이다.

root에서 변수들을 '--' 과 '이름'으로 구체화 할 수 있다. 

위의 코드처럼 쓰고나면 팀끼리 이 변수를 공유할 수 있다. 

```css
@custam-selector:--headrs h1, h2, h3, h4, h5, h6
```

위 처럼 쓰고 variable을 구체화 하는 것이다. 

```css
:--headers{
	color:yellow
	}
```

header을 불러서 color을 적용시킨다.

html의 h1, h2, h3, h4, h5, h6에 적용이 되는 것이다. 



### 3.4 @custom-media and Media Query Ranges

```css
@custom-media --ipad-size (width<=850px);
@media (--ipad-size){
    body{
        background-color:red;
    }
}
```

이렇게 지정하게 되면 화면이 ipad-size인 850px보다 작거나 같게 되었을 때  background가 red가 된다. (width<=850px) 뒤에 (width<=850px) and를 쓰고 크거나 같다 작다 이런식으로 범위를 더 지정해줄 수 있다.  또한 (450<=width<850px) 이렇게 범위를 지정할 수도 있다.

이것을 Media Query Ranges라 부른다.





### 3.5 color-mod, gray(), system-ui

color mod: 색을 수정하게 할 수 있도록 하는 것

https://www.w3.org/TR/css-color-4/#numeric-rgb 

위의 사이트에 접속하면 colormod를 사용해 다양한 키워드를 더 빠르게 css의 색상을 변경할 수 있다. 

```css
h1{
    color:color-mod(#f1c40f alpha(50%));
}
```

색상은 같지만 50%의 투명도로 나온다. 

```css
h1{
    color:#f1c40f;
}

h1: hover{
    color:color-mod(#f1c40f lightness(80%));
}
```

위의 코드를 쓰게되면 마우스를 올렸을 때 80% 의 투명도로 바뀌는 효과를 낼 수 있다. 

```css
h1{
    font-family:color:system-ui;
}
```

system-ui는 사용자의 컴퓨터에 설치되어이쓴 font들로의 지름길이다.





### 3.6 Nesting Rules

nesting: selector의 반복을 줄일 수 있다.

```css
main{
    background-color:blue;
}

main section{
    
}
```

or

```css
main{
    background-color:blue;
    & section{
        background-color: red;
        width 500px;
}
```



```css
main{
    background-color:blue;
    & section{
        background-color: red;
        width 500px;
        &li{
            ackground-color: yellow;
            width 400px;
            &a{
                color: white;
                &:hover{
                    font-size: 30px;
                }
            }
        }
    }
}
a{
    color: red;
}
```

css에서는 selection이 더 자세할 수록 우위를 가진다. 그렇기 때문에 a{}에  있는 red는 적용되지 않는다. 



### 3.7 Conclusions

css grid kiss: grid areas와 grid templates에 해당하는 css를 매우 쉽게 그리게 해준다. 
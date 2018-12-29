# CSS Grid

#### Why we need Grid

flexbox는 웹 사이트에서 필요로하는 레이아웃들을 생성할 때 부족한 부분이 있어 css gird를 사용한다. (간격 조정 문제 등)

#### Basics CSS Grid

Grid의 문법은 flexbox와 매우비슷

Grid에는 row와 column이 있고 이것을 정의 하는 것은 밑의 코드와 같다.

```css
.father{
    display: grid;
	grid-template-columns:30px;
	grid-template-rows:30px;    
}
```

30px*30px의 정사각형을 하나 만들 수 있다.  father이 단 하나의 row/column을 가지고 있기 때문에.

```css
.father{
    display: grid;
	grid-template-columns:30px 50px;
	grid-template-rows:30px 12px;    
}
```

이렇게 하게되면 총 4칸으로 이루어진 레이아웃이 생성된다.

30,30/ 30,50/30,12/50,12 

```css
grid-gap: 5px;
```

레이아웃에 gap을 주는것이다.

#### Auto Rows and Columns

설정해 놓은 rows와 columns보다 더 많은 element들이 만들어져서 자리에 맞지 않는다면 나머지의 element의 자리는 auto rows/columns로 설정 해줄 수 있다.

```css

```

나머지 element의 rows를 60px로 지정하겠다는 이야기이다. column은 기존에 설정 했던 값으로 정렬된다.

```css
gird-auto-columns:60px;
```

나머지 element의 columns를 60px로 지정하겠다는 이야기이다. rows는 기존에 설정 했던 값으로 정렬된다.

```css
gird-auto-flow:row;
```

gird-auto-flow는 row와 column을 사용한다.위의 코드는 정의되지 않은 elements에 대해서는 row에 자동으로 놓겠다는 의미이다. (column으로 바꿀 수 있다. )

#### Grid Template Areas

```css
gird-template-areas: "header header header"
					 "content content sidebar"
					 "content content sidebar"
					 "footer footer footer";
```

css에서 무언갈 그릴 수 있게 해준다.

위의 코드의 의미는 header이 한줄을 차지하고 두줄은 content와 sidebar이 차지하고 footer이 한줄을 차지한다는 의미이다. (공간의 생성)

첫째 줄에는 header을 세번 적어넣었기 때문에 column을 세개 만들겠다고 선언한 것과 같음.

둘째, 셋째 줄에는 content두개와 sidebar하나로 이루어진 column을 만들고 첫째 줄과 같은 높이를 두개 만들겠다고 선언한 것과 같음.

네번째 줄에는 footer세개를 만들겠다고 선언한 것과 같음

```css
.first{
    grid-area: header;
    background-color: #f1c40f;
}
```

first클래스에서 grid-area를 header로 주게되면 첫번째 줄(세개의 column)을 모두 header이 차지하게 된다.

![1546084317026](C:\Users\세희\AppData\Roaming\Typora\typora-user-images\1546084317026.png)

이 기능을 활용하면 화면에 공간을 그린 다음 채우는 일을 할 수 있다. width나 height,margin,top등의 속성을 일일이 정해주지 않아도 알아서 제자리를 찾아감.



#### fr and repeat()

```css
grid-template-columns:2fr 1fr 2fr 1fr
```

fraction: gird에서 사용하는 새로운 측정단위로 간단히 말하면 자리를 차지하는 것이다.  상대적인 자리 차지 (2:1:2:1)

grid-template-columns: 얼마나 많은 fr을 사용자가 가지고 있는 지 등을 정의 해 놓을 수 있는 것이다.

```css
grid-template-columns:repeat(5, 1fr);
```

위의 코드는 1fr을 다섯번반복 하겠다는 뜻이다 1:1:1:1:1

#### minmax, max-content, min-content

minmax: 사용자가 이용할 object의 maximum과 minmum의 크기를 지정해주는 도구이다. 

```css
grid-template-columns:minmax(400px, 2fr) repeat(3, 1fr);
```

object가 가져야 할 최소 크기를 정할 수 있다. 즉 화면의 크기가 줄더라도 400px 만큼은 그대로 유지한다는 것이다.

```css
grid-template-columns:max-content repeat(3, 1fr);
```

max-content 레이아웃 안에 있는 content를 기반으로 최대 크기를 정하는 것이 핵심이다. 

만약 content가 글이라면 글이 밑으로 넘어가는 일 없이 한줄로 쓰여진다. ("내가 가질 수 있는 최대의 공간을 갖겠다")

```css
grid-template-columns:min-content repeat(3, 1fr);
```

min-content 레이아웃 안에 있는 content를 기반으로 최소 크기를 정하는 것이 핵심이다.  ("가장적은 공간만을 사용하라")

#### auto-fill, auto-fit

```css
grid-template-columns:repeat(auto-fill,50fr);
```

fraction하나가 전체의 공간을 다 차지하게 되는 것이다. 위의 코드는 가질 수 있는 가장 많은 column을 가지되 50px로 하겠다는 의미이다.

```css
grid-template-columns:repeat(auto-fill,340fr);
```

340px크기로 이루어진 div를 다섯번 반복 할 수 없기 때문에 나누어서 밑으로 들어간다.

단범은 크기에 대한 유연성이 없다는 것이다.

```css
grid-template-columns:repeat(auto-fit, minmax(350px,1fr));
```

이런 문제점을 보완하기 위해 minmax를 쓴다. 최소값은350px로 지정하고 최대값을 1fr로 지정된다. 

```css
grid-template-columns:repeat(auto-fill, minmax(50px,1fr));
```

auto-fill은 기존에 있는 layout을 채워나가는 방식으로 가능한 많은 cell로 container을 꽉 채우는데 gost grid가 생길 수 있다.

  

```css
grid-template-columns:repeat(auto-fit, minmax(50px,1fr));
```

ghost grid를 만들지 않고 content를 받아와서 빈자리를 모두채울 때 까지 펼쳐준다.

#### Justify Content, Align Content and place Content

```css
justify-content: center;
```

모든 박스가 중앙으로 정렬된다.

```css
justify-content: start;
```

모든 박스가 왼쪽으로 정렬된다.

```css
justify-content: end;
```

모든 박스가 오른쪽으로 정렬된다.

```css
align-content: center;
```

모든 박스가 높이를 기준으로 중앙으로 정렬된다.(+ start, end)

align은 모든 box가 포함되어 있는 grid container을 이동시키는 것이다.

```css
place-conten: center end;
```

place-content의 첫번째  argument는align-content(넓이기준)값이고 두번째는  justift-content(높이기준)의 값이다.

#### Justift Items, Align Items and Place Items



```css
justify-item: center;
```

container은 그대로 이고 그 안의 item만을 움직이다.

 만약 box안의 item이 숫자 2였다면 박스의 넓이를 기준으로 정중앙으로 2가 정렬되는 것이다.

```css
align-item: center;
```

만약 box안의 item이 숫자 2였다면 박스의 높이를 기준으로 정중앙으로 2가 정렬되는 것이다.

```css
place-items:
```

첫번째 argument에는 vertical한 값을, 두번째는 horizontal한 값을 넣을 수 있다.

이것이 바로 grid 내부에서 혹은 box내부에서의 element를 움직이는 방법이다.
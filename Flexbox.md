# Flexbox

#### why we need Flexbox

계산을 하지 않아도 flexbox가 알아서 간격조정등의 웹사이트 들이 필요로하는 기능을 제공



#### Baisic of Flexbox

```css
body{
    display: flex;
}
```

플렉스컨테이너 규칙을 따른다.

```css
justify-content: space-between;
```

반응형으로 페이지 구성한다. 기기와 상관없이 간격 맞춤

```css
flex-end;
```

오른쪽으로 정렬

```css
flex-start;
```

왼쪽으로 정렬



#### Main Axis and Cross Axis

```css
align-items:center;
```

main axis: justify-content가 영향을 주는 축

cross axis : align-item이 영향을 주는 축

display: flex 옵션은 기본적으로 row로 방향이 결정되어있음

어디에 element를 놓을 것인지

flex-direction: row; 가로정렬

flex-direction:column; 세로정렬

flex-direction의 옵션을 변경하면 main-axis와 cross-axis는 서로 바뀜

main-axis와 cross-axis는 그대로 두고 수평 수직 성질을 거꾸로 바꾸기



#### Flex Wrap and Direction

flex-wrap: flex가 하는 일이다. 내부의 아이템들이 잘 맞지 않았을 때 사용한다.(이미지가 찌그러지지 않게함)

```css
flex-wrap: wrap;
```

이렇게 하지 않았을 때는 아이템들을 최대한 압축하여 한 줄에 모든 아이템이 들어오도록 하지만 flex-wrap: wrap;을 하게되면 내가 설정한 옵션 값을 따른다.

flex direction: flex 아이템이 flex father이 되도록 하는 기능(옵션을 가지게하는 것)

```css
flex-direction: row-reverse
```

reverse를 사용하면 아이템의 위치가 반대로 바뀌게 된다.(123->321)



#### Align Self and Flexbox Conclusions

align-self: 각각의 아이템에 대해서 정렬을 하는데  father에게 주어지는 옵션이 아닌 아이템들에게 직접 옵션을 준다.

```css
align-self: flex-end;
```

오직 하나의 아이템만 움직임.
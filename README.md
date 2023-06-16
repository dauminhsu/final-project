<!-- 
# <center>🔥   <span style="color:lightcoral">Финальный проект</span>   🔥</center>

## <center>🔶 <span style="color:moccasin">Простое графическое приложение</span> 🔶</center>


### 💠 Введение

1. Đây là một ứng dụng Web cho phép người dùng vẽ các đồ thị đơn giản trên một trang Web và lưu lại dưới dạng hình ảnh. Ứng dụng được viết bằng ngôn ngữ Python và HTML.

2. Tại vì đây chỉ là một ứng dụng vẽ đồ thị đơn giản nên chúng tôi đã lập trình cho chương trình của mình 4 chức năng chính:
    - Vẽ điểm 
    - Vẽ đoạn thẳng
    - Vẽ đa giác
    - Vẽ hình tròn 

### 💠 Необходимые условия для использования проекта
1. Bạn phải có ít nhất 1 ứng dụng để viết mã trên máy tính của mình.
2. Có kiến thức cơ bản về ngôn ngữ lập trình Python.
3. Bạn có hiểu biết cơ bản về lý thuyết đồ thị.


### 💠 Идея

1. Dựa trên nội dung:
    - Lab_7: Vẽ đồ thị sử dụng thư viện Matplotlib 
    - Lab_9: Tạo một ứng dụng Web sử dụng Flask

##### 🔻*Chúng tôi đã tạo ra một ứng dụng Web có thể vẽ được những đồ thị (hình vẽ đơn giản) như chúng tôi đã đề cập ở phần Введение[^1].*
[^1]: Введение


### 💠 Алгоритм

1. Chúng tôi sẽ tạo ra một <span style="color:aquamarine">*List*</span> chứa những điểm mà người dùng nhập vào từ trang Web.
2. Với những hình vẽ chúng tôi có một thuật toán như sau:
    - Điểm: Là một tập hợp gồm có 2 tọa độ (x, y)
    - Đoạn thẳng: Là một tập hợp gồm có 2 điểm (A, B) được nối với nhau. Hai điểm này được tạo nên từ 4 tọa độ A(x_A, y_A) và B(x_b, y_B)
    - Đa giác: Là một tập hợp gồm nhiều điểm được nối với nhau bằng các đoạn thẳng 
    - Hình tròn: Là tập hợp các điểm trong mặt phẳng cách đều một điểm cho trước, điểm này được gọi là tâm  của đường tròn (thường được kí hiệu là: O(x, y)) và khoảng cách từ tâm đến 1 điểm bất kì trong tập hợp được gọi là bán kính của đường tròn (thường được kí hiệu là: R)


### 💠 Инструкции по использованию:

1. Truy cập vào trang web của ứng dụng.
2. Nhập tên loại đồ thị mà bạn muốn vẽ, ví dụ như:
    - Vẽ điểm: Point(-3, 5)
    - Vẽ đoạn thẳng: Segment A(7,5) B(11,3)
    - Vẽ đa giác (đa giác là một hình gồm nhiều cạnh và nhiều đỉnh, vì thế sẽ có rấ nhiều loại đa giác mà bạn có thể vẽ được), ví dụ:
        - Hình tam giác: segment A(1,2) B(3,4) C(5,6)
        - Hình tứ giác : segment A(1,2) B(3,4) C(5,6) D(7,8)
        - Vân vân ...
    - Vẽ hình tròn: circle O(3,3) 5
3. Sau khi nhập xong hình bạn muốn vẽ, hãy nhấn vào nút  <span style="color:palegreen">*"Обновлять"*</span> 
4. Nếu bạn muốn xóa những hình vẽ mà bạn đã vẽ thì nhấn vào nút <span style="color:red">*"Очистить"*</span>

### 💠 Системные требования

1. Để có thể chạy được chương trình trên máy tính của bạn, cần:
    - Cài đặt trình biên dịch cho ngôn ngữ Python
    - Cài đặt các thư viện: flask, matplotlib

### 💠 Запустите приложение

> Chạy ứng dụng bằng lệnh sau:
    ```
    python app.py 
    ```

 -->


 # <center>🔥   <span style="color:lightcoral">Финальный проект</span>   🔥</center>

## <center>🔶 <span style="color:moccasin">Простое графическое приложение</span> 🔶</center>


### 💠 Введение

1. Это веб-приложение, которое позволяет пользователям рисовать простые графики на веб-странице и сохранять их в виде изображений. Приложение написано на языках Python и HTML.

2. Поскольку это простое приложение для рисования графиков, мы написали 4 основных функции для нашей программы:
    - Рисование точки
    - Рисование отрезка
    - Рисование многоугольника
    - Рисование круга

### 💠 Необходимые условия для использования проекта

1. Вам нужно иметь хотя бы одно приложение для написания кода на вашем компьютере.
2. Необходимо иметь базовые знания языка программирования Python.
3. Вы должны иметь базовое понимание теории графов.


### 💠 Идея

1. На основе содержания:
    - Lab_7: Рисование графиков с использованием библиотеки Matplotlib
    - Lab_9: Создание веб-приложения с использованием Flask

##### 🔻Мы создали веб-приложение, которое может рисовать графики (простые рисунки), как мы упоминали в разделе Введение[^1].
[^1]: Введение

### 💠 Алгоритм

1. Мы создадим список <span style="color:aquamarine">*List*</span>, который будет содержать точки, введенные пользователем на веб-странице.
2. Для наших рисунков у нас есть следующий алгоритм:
    - Точка: это набор из 2 координат (x, y)
    - Отрезок: это набор из 2 точек (A, B), соединенных между собой. Эти две точки состоят из 4 координат: A(x_A, y_A) и B(x_b, y_B).
    - Многоугольник: это набор из нескольких точек, соединенных между собой отрезками.
    - Круг: это набор точек в плоскости, расположенных на равном расстоянии от заданной точки, называемой центром окружности (обычно обозначается как: O(x, y)), и расстояние от центра до любой точки в наборе называется радиусом окружности (обычно обозначается как: R)


### 💠 Инструкции по использованию:

1. Зайдите на веб-сайт приложения.
2. Введите название типа графика, который вы хотите нарисовать, например:
    - Рисование точки: Point(-3, 5)
    - Рисование отрезка: Segment A(7,5) B(11,3)
    - Рисование многоугольника (многоугольник - это фигура с несколькими сторонами и вершинами, поэтому существует много различных типов многоугольников, которые вы можете нарисовать), например:
        - Треугольник: segment A(1,2) B(3,4) C(5,6)
        - Четырехугольник: segment A(1,2) B(3,4) C(5,6) D(7,8)
        - И т.д.
    - Рисование круга: circle O(3,3) 5
3. После того, как вы ввели график, который вы хотите нарисовать, нажмите кнопку <span style="color:palegreen">*"Обновлять"*</span>.
4. Если вы хотите удалить нарисованные вами фигуры, нажмите кнопку <span style="color:red">*"Очистить"*</span>

### 💠 Системные требования

1. Чтобы запустить программу на вашем компьютере, нужно:
    - Установить компилятор для языка Python
    - Установить библиотеки: flask, matplotlib

### 💠 Запустите приложение

- Запустите приложение с помощью следующей команды:
    ```
    python app.py 
    ```

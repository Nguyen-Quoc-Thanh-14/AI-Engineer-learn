---
title: "TẬP 00 — NỀN TẢNG TOÁN HỌC CHO PYTHON VÀ AI"
subtitle: "Từ kiến thức phổ thông đến Machine Learning, Deep Learning và Computer Vision"
author: "Bộ tài liệu tự học Python & AI Engineer"
date: "08/11/2026"
lang: vi-VN
toc-title: "MỤC LỤC"
---

**Giáo trình thuần lý thuyết · Có lập luận, ví dụ tính tay và liên hệ ứng dụng**

**Đối tượng:** người học từ căn bản, chuẩn bị nghiên cứu Python, dữ liệu, Machine Learning (ML), Deep Learning (DL) và Computer Vision (CV). **Vị trí:** đọc trước Tập 01–05; có thể quay lại từng chương khi cần.

> **Quy ước học thuật.** Một *định nghĩa* quy định ý nghĩa thuật ngữ; một *định lý* cần chứng minh trong hệ giả thiết rõ ràng; một *ví dụ tính tay* chỉ minh họa trường hợp cụ thể; một *kiểm thử chương trình* chỉ cung cấp bằng chứng thực nghiệm với môi trường và dữ liệu đã chạy. Không đánh đồng bốn cấp độ này. Các công thức trong sách sử dụng quy ước toán học thông dụng; chúng không phải cam kết hành vi của mọi thư viện hay mọi phiên bản Python.

## Cách đọc tài liệu

- **Khái niệm và ký hiệu:** hiểu đối tượng đang xét, miền giá trị, đơn vị và các giả thiết.
- **Công thức và cơ chế:** đọc bằng lời, nhận diện từng biến và cách các thành phần liên hệ.
- **Chứng minh hoặc lập luận:** đi từ giả thiết, qua bước hợp lệ, tới kết luận; đối với kết quả nâng cao sẽ ghi rõ *phác thảo lập luận* nếu chưa chứng minh đầy đủ.
- **Ví dụ tính tay:** tự tính một trường hợp nhỏ trước khi nghĩ đến viết mã.
- **Liên hệ AI và giới hạn:** hiểu kiến thức dùng ở đâu, cũng như điều kiện khiến công thức không áp dụng.

## Nội dung 15 chương

1. Ngôn ngữ toán học và cách chứng minh.
2. Số, đại số, lũy thừa và tổng.
3. Hàm số, đồ thị và mô hình hóa.
4. Giải tích một biến: biến thiên liên tục.
5. Đại số tuyến tính và biểu diễn dữ liệu.
6. Giải tích nhiều biến và tối ưu hóa.
7. Xác suất: mô tả bất định.
8. Thống kê, lấy mẫu và đánh giá bằng chứng.
9. Lý thuyết thông tin và hàm mất mát.
10. Toán số trên máy tính.
11. Từ toán đến Machine Learning.
12. Deep Learning: đạo hàm qua mạng nhiều lớp.
13. Toán học cho Computer Vision.
14. Phép đo chất lượng và khả năng khái quát hóa.
15. Bản đồ tổng hợp: học toán để đọc AI.

## Lộ trình theo mức độ

- **Chặng 1 — Nền móng (Chương 1–3):** ký hiệu, logic, phép biến đổi, hàm số.
- **Chặng 2 — Toán liên tục (Chương 4–5):** đạo hàm, gradient, tích phân, vector và ma trận.
- **Chặng 3 — Mô hình và dữ liệu (Chương 6–9):** tối ưu hóa, xác suất, thống kê, thông tin.
- **Chặng 4 — Máy tính và thuật toán (Chương 10–11):** sai số, độ phức tạp tính toán, hồi quy và phân loại.
- **Chặng 5 — AI và thị giác máy tính (Chương 12–14):** mạng neural, lan truyền ngược, tích chập và tensor.
- **Chặng 6 — Tổng hợp (Chương 15):** kết nối thành quy trình tư duy hoàn chỉnh.

# Chương 1. Ngôn ngữ toán học và cách chứng minh

## 1.1. Tập hợp, phần tử, mệnh đề và ký hiệu

**Định nghĩa.** *Tập hợp* là một nhóm đối tượng được xác định rõ. Ký hiệu $x\in A$ đọc là “$x$ thuộc tập $A$”; $x\notin A$ là “không thuộc”. Các tập thường gặp gồm $\mathbb N$ (số tự nhiên; sách này lấy $0\in\mathbb N$), $\mathbb Z$ (số nguyên), $\mathbb R$ (số thực). Ký hiệu $A\subseteq B$ nói rằng mọi phần tử của $A$ cũng thuộc $B$.

Một *mệnh đề* là phát biểu có giá trị đúng hoặc sai khi ngữ cảnh xác định. “$x>0$” chưa phải mệnh đề đầy đủ nếu chưa biết $x$ là gì. “Với mọi $x\in\mathbb R$, $x^2\geq0$” là mệnh đề đúng.

Các ký hiệu quan trọng: $\forall$ (với mọi), $\exists$ (tồn tại), $\Rightarrow$ (suy ra), $\Leftrightarrow$ (tương đương), $\land$ (và), $\lor$ (hoặc), $\neg$ (phủ định). Phân biệt “$P\Rightarrow Q$” với “$Q\Rightarrow P$”: hai hướng không tự động cùng đúng.

**Ví dụ.** Nếu $x=2$ thì $x^2=4$ và $x>0$. Nhưng $x^2=4$ không suy ra $x>0$ vì $x=-2$ cũng thỏa mãn. Đây là **phản ví dụ** cho suy luận đảo chiều.

**Liên hệ AI.** Điều kiện dữ liệu đầu vào như “mọi nhãn đều là số nguyên từ 0 đến $K-1$” là giả thiết có thể kiểm tra. Nếu bỏ qua, công thức hoặc phép tính loss có thể vô nghĩa.

## 1.2. Điều kiện cần, điều kiện đủ và tương đương

**Định nghĩa.** $P$ là **điều kiện đủ** cho $Q$ khi $P\Rightarrow Q$. $Q$ là **điều kiện cần** cho $P$ trong cùng phát biểu. Hai mệnh đề tương đương khi cả hai chiều đều đúng: $P\Leftrightarrow Q$.

**Ví dụ.** Với $n\in\mathbb Z$, “$n$ chia hết cho 4” là điều kiện đủ để “$n$ chẵn”; ngược lại không đúng vì 6 chẵn nhưng không chia hết cho 4.

**Kỹ thuật phản chứng.** Muốn chứng minh $P\Rightarrow Q$, có thể giả sử $P$ đúng và $Q$ sai rồi suy ra mâu thuẫn. Chẳng hạn không tồn tại số nguyên lẻ có bình phương chẵn: đặt $n=2k+1$ thì $n^2=4k(k+1)+1$ là số lẻ.

**Giới hạn.** Phản chứng chỉ dùng được khi hệ logic và giả thiết rõ ràng. Trong các bài toán thực nghiệm, quan sát chưa thấy phản ví dụ không phải chứng minh phổ quát.

## 1.3. Quy nạp toán học: từ trường hợp đầu đến mọi số tự nhiên

**Định lý.** Với mọi $n\in\mathbb N$,

$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}.$$

**Chứng minh bằng quy nạp.** Bước cơ sở $n=0$: vế trái là tổng rỗng bằng 0; vế phải bằng 0. Bước quy nạp: giả sử đúng tại $n=k$, tức $1+\cdots+k=k(k+1)/2$. Khi đó

$$\sum_{i=1}^{k+1}i=\frac{k(k+1)}2+(k+1)=\frac{(k+1)(k+2)}2.$$

Vậy mệnh đề đúng với $k+1$. Từ bước cơ sở và bước chuyển, mệnh đề đúng với mọi số tự nhiên.

**Ý nghĩa.** Quy nạp không phải kiểm tra lần lượt từng số. Ta chứng minh một cơ chế bảo toàn tính đúng khi tăng $n$.

**Liên hệ lập trình.** Lập luận bất biến vòng lặp có cấu trúc tương tự: đúng trước khi lặp; nếu đúng đầu vòng thì vẫn đúng sau một bước; khi kết thúc, bất biến kết hợp điều kiện dừng cho ra kết quả.

## 1.4. Bất biến, tiền điều kiện và hậu điều kiện

**Khái niệm.** *Tiền điều kiện* mô tả dữ liệu ban đầu hợp lệ; *hậu điều kiện* là mục tiêu sau khi thuật toán chạy; *bất biến* là điều luôn đúng tại những thời điểm lặp đã định.

**Ví dụ tổng dãy.** Giả sử cần tính $S_n=\sum_{i=1}^{n} i$ với $n\geq0$. Tại thời điểm đã xử lý $k$ số, dùng bất biến $S=\sum_{i=1}^{k}i$. Khởi tạo $k=0,S=0$ thì bất biến đúng. Mỗi bước cập nhật $k\leftarrow k+1$, $S\leftarrow S+k$, nên bất biến vẫn đúng. Khi dừng tại $k=n$, hậu điều kiện $S=S_n$ được chứng minh.

**Điểm dễ nhầm.** Chứng minh một bất biến không đủ để chứng minh chương trình *kết thúc*. Cần thêm đại lượng tiến triển như $n-k$ là số nguyên không âm và giảm mỗi vòng.

**Liên hệ AI.** Trong xử lý minibatch, có thể giữ bất biến “đã tính đúng tổng loss của các mẫu đã xét”. Tính đúng các phép cộng vẫn khác với chất lượng của mô hình học máy.

# Chương 2. Số, đại số, lũy thừa và tổng

## 2.1. Số thực, phân số, thứ tự và miền xác định

Số nguyên, hữu tỉ và thực có các quy tắc phép cộng/nhân quen thuộc. Số thực bao gồm cả các số vô tỉ như $\sqrt{2}$, $\pi$. **Miền xác định** của biểu thức là tập giá trị khiến biểu thức có nghĩa.

**Ví dụ.** $f(x)=1/(x-2)$ xác định khi $x\ne2$. $g(x)=\sqrt{x}$ trên số thực chỉ xác định khi $x\ge0$. $h(x)=\ln x$ đòi hỏi $x>0$. Bỏ qua miền xác định là nguồn gốc của nhiều lỗi “chia cho 0”, “NaN”, “log giá trị âm”.

**Quy tắc biến đổi bất đẳng thức.** Nếu $a<b$ thì $a+c<b+c$. Nhân với số dương giữ nguyên chiều; nhân với số âm phải đảo chiều. Chẳng hạn từ $-2<1$ nhân với $-3$ được $6>-3$.

**Liên hệ AI.** Các phép chuẩn hóa như $(x-\mu)/\sigma$ đòi hỏi $\sigma\ne0$. Với dữ liệu có độ lệch chuẩn bằng 0, cần quy tắc xử lý riêng.

## 2.2. Lũy thừa, căn bậc hai và logarit

Với $a>0$ và số mũ thực $x$, lũy thừa $a^x$ có các tính chất $a^{x+y}=a^xa^y$ và $(a^x)^y=a^{xy}$. Logarit $\log_a b$ với $a>0,a\ne1,b>0$ là số $t$ thỏa $a^t=b$.

$$\log_a(xy)=\log_a x+\log_a y,\qquad \log_a(x^r)=r\log_a x.$$

**Lập luận.** Đặt $x=a^u$, $y=a^v$; khi ấy $xy=a^{u+v}$, nên $\log_a(xy)=u+v=\log_a x+\log_a y$.

Ký hiệu $\ln x$ là logarit tự nhiên cơ số $e\approx2{,}71828$. Trong ML, $\ln$ xuất hiện trong log-likelihood và cross-entropy. Log biến tích xác suất nhỏ thành tổng log, giúp tính toán ổn định hơn.

**Giới hạn.** Không dùng $\ln0$ hay $\ln$ của số âm trong miền số thực. Công thức log-sum-exp cần kỹ thuật trừ giá trị lớn nhất để hạn chế tràn số.

## 2.3. Tổng hữu hạn, ký hiệu sigma và tổng cấp số nhân

Ký hiệu $\sum_{i=1}^{n}a_i$ là tổng các hạng $a_1,\ldots,a_n$. Chỉ số $i$ là biến chạy; $n$ là cận trên. Với cấp số nhân, đặt $S_n=1+r+\cdots+r^{n-1}$.

**Chứng minh.** Với $r\ne1$, nhân cả hai vế với $r$ rồi lấy $S_n-rS_n$: mọi số hạng ở giữa triệt tiêu, còn $1-r^n$. Suy ra

$$S_n=\frac{1-r^n}{1-r}\quad(r\ne1).$$

Nếu $r=1$ thì $S_n=n$. Nếu $|r|<1$, giới hạn $r^n\to0$, dẫn tới tổng vô hạn $1/(1-r)$.

**Liên hệ AI.** Trung bình cộng, hàm mất mát trên tập mẫu và kỳ vọng rời rạc đều là các dạng tổng. Ví dụ $L=(1/n)\sum_{i=1}^n \ell_i$ là loss trung bình trên $n$ mẫu.

## 2.4. Trung bình có trọng số và chuẩn hóa

Cho các giá trị $x_i$ với trọng số không âm $w_i$. Trung bình trọng số là

$$\bar x_w=\frac{\sum_i w_ix_i}{\sum_i w_i},\quad\sum_i w_i>0.$$

Nếu đặt $\alpha_i=w_i/\sum_jw_j$, ta có $\alpha_i\ge0$, $\sum_i\alpha_i=1$ và $\bar x_w=\sum_i\alpha_ix_i$. Khi đó $\bar x_w$ nằm giữa giá trị nhỏ nhất và lớn nhất của các $x_i$, vì đó là một **tổ hợp lồi**.

**Ví dụ.** Điểm 7 có trọng số 2, điểm 9 có trọng số 1: $(2\cdot7+1\cdot9)/3=23/3\approx7{,}67$.

**Liên hệ AI.** Attention dùng các trọng số chuẩn hóa để trộn các vector giá trị. Tuy nhiên trọng số attention được học theo ngữ cảnh chứ không mang mặc định ý nghĩa nhân quả.

# Chương 3. Hàm số, đồ thị và mô hình hóa

## 3.1. Hàm số là một ánh xạ, không chỉ là công thức

**Định nghĩa.** Hàm $f:A\to B$ gán mỗi $x\in A$ đúng một giá trị $f(x)\in B$. $A$ là *miền xác định*, $B$ là *tập đích*, còn tập các giá trị thực sự đạt được là *tập giá trị*.

**Ví dụ.** $f(x)=x^2$ xác định trên $\mathbb R$. Ta có $f(-2)=f(2)=4$, vì vậy hàm không đơn ánh trên toàn $\mathbb R$. Nếu thu hẹp miền thành $x\ge0$ thì nó đơn ánh và có hàm ngược $f^{-1}(y)=\sqrt y$ với $y\ge0$.

**Chú ý ký hiệu.** $f$ là hàm; $f(x)$ là giá trị tại $x$; $f^{-1}$ thường là hàm ngược, không phải $1/f$.

**Liên hệ AI.** Một mô hình dự đoán có thể được xem là $f_\theta:X\to Y$, trong đó $\theta$ là tập tham số và $X,Y$ là không gian đầu vào/đầu ra.

## 3.2. Hàm hợp và đường đi của dữ liệu

Cho $g:A\to B$ và $f:B\to C$, hàm hợp $(f\circ g)(x)=f(g(x))$. Muốn hợp lệ, đầu ra của $g$ phải phù hợp miền của $f$.

**Ví dụ.** $g(x)=2x+1$, $f(t)=t^2$ thì $(f\circ g)(x)=(2x+1)^2$. Nhưng $(g\circ f)(x)=2x^2+1$; nhìn chung hai phép hợp không hoán đổi.

**Liên hệ AI.** Mạng neural nhiều lớp là hợp của những biến đổi: dữ liệu đầu vào $\to$ phép biến đổi tuyến tính $\to$ hàm kích hoạt $\to$ lớp tiếp theo. Backpropagation thực chất áp dụng quy tắc đạo hàm cho chuỗi hàm hợp này.

## 3.3. Hàm tuyến tính, affine và mô hình đơn giản

Hàm tuyến tính trong đại số tuyến tính phải thỏa $T(x+y)=T(x)+T(y)$ và $T(cx)=cT(x)$. Trong trường hợp một chiều $T(x)=wx$. Hàm $f(x)=wx+b$ với $b\ne0$ là **affine**, không tuyến tính theo nghĩa chặt.

**Ví dụ.** Doanh thu $R(q)=pq$ là tuyến tính theo số lượng $q$ nếu đơn giá $p$ cố định. Chi phí $C(q)=cq+F$ là affine nếu có chi phí cố định $F$.

**Liên hệ AI.** Một lớp dense trước activation thường tính $z=Wx+b$; tên “lớp tuyến tính” trong tài liệu kỹ thuật có thể gọi tắt cả phép affine, nhưng cần phân biệt khi chứng minh tính chất toán học.

## 3.4. Đơn điệu, cực trị và độ cong

Hàm $f$ **đồng biến** trên khoảng nếu $x_1<x_2$ suy ra $f(x_1)\le f(x_2)$. **Nghịch biến** khi bất đẳng thức đảo chiều. Điểm cực tiểu cục bộ có giá trị không lớn hơn các giá trị đủ gần, không nhất thiết là nhỏ nhất toàn miền.

**Ví dụ.** $f(x)=(x-3)^2+2\ge2$ với mọi $x$, và bằng 2 khi $x=3$: đây là cực tiểu toàn cục. Biểu thức tổng bình phương là dạng cơ bản của nhiều hàm mất mát.

**Liên hệ AI.** Mục tiêu huấn luyện là giảm loss. Nếu loss không lồi, việc gradient bằng 0 không bảo đảm tìm được cực tiểu toàn cục.

# Chương 4. Giải tích một biến: biến thiên liên tục

## 4.1. Giới hạn và tính liên tục

Ta viết $\lim_{x\to a}f(x)=L$ nếu giá trị của $f(x)$ tiến gần $L$ khi $x$ tiến gần $a$, không phụ thuộc việc $f(a)$ có được định nghĩa hay không. Hàm liên tục tại $a$ nếu $f(a)$ xác định và giới hạn bằng $f(a)$.

**Ví dụ.** Với $x\ne1$, $(x^2-1)/(x-1)=x+1$, nên giới hạn khi $x\to1$ là 2 dù biểu thức ban đầu không xác định tại 1.

**Phân biệt.** “Giới hạn hữu hạn” không đồng nghĩa “biểu thức có thể thay trực tiếp giá trị”. Cần kiểm tra miền xác định và trường hợp dạng $0/0$.

**Liên hệ AI.** Giới hạn nằm sau đạo hàm, gradient và phương pháp tối ưu. Trong tính toán máy, ta không dùng các số vô hạn nhỏ thật sự mà dùng phép gần đúng với sai số.

## 4.2. Đạo hàm là tốc độ thay đổi cục bộ

**Định nghĩa.** Nếu tồn tại giới hạn,

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h.$$

Tử số là mức thay đổi đầu ra, mẫu số là mức thay đổi đầu vào. Đạo hàm mô tả độ dốc của tiếp tuyến hoặc tốc độ biến thiên tức thời.

**Chứng minh cho $f(x)=x^2$.**

$$\frac{(x+h)^2-x^2}{h}=\frac{2xh+h^2}{h}=2x+h.$$

Khi $h\to0$, giới hạn là $2x$. Vậy $(x^2)'=2x$. Chứng minh này giả sử tính đạo hàm trên $\mathbb R$ và dùng các phép biến đổi khi $h\ne0$.

**Liên hệ AI.** Đạo hàm loss theo tham số cho biết thay đổi một chút tham số sẽ ảnh hưởng loss theo hướng nào, nếu loss khả vi gần điểm đang xét.

## 4.3. Quy tắc tích, thương và hàm hợp

Với các hàm khả vi $u,v$:

$$(u+v)'=u'+v',\quad(uv)'=u'v+uv',$$

$$\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}\quad(v\ne0).$$

**Quy tắc dây chuyền:** nếu $y=f(g(x))$ thì $y'=f'(g(x))g'(x)$.

**Lập luận trực giác.** Thay đổi nhỏ $\Delta x$ tạo $\Delta g\approx g'(x)\Delta x$; sau đó $\Delta y\approx f'(g(x))\Delta g$. Kết hợp thu được $\Delta y/\Delta x\approx f'(g(x))g'(x)$. Một chứng minh chính thức cần kiểm soát phần sai số khi $\Delta x\to0$.

**Ví dụ.** $y=(3x+1)^2$: $y'=2(3x+1)\cdot3=6(3x+1)$. Nếu quên nhân đạo hàm “hàm bên trong”, kết quả sai.

## 4.4. Đạo hàm của mũ và logarit

Hai công thức quan trọng:

$$\frac{d}{dx}e^x=e^x,\qquad \frac{d}{dx}\ln x=\frac1x\quad(x>0).$$

Với $a>0$, $(a^x)'=a^x\ln a$. Với hàm hợp dương $g(x)$, $\frac{d}{dx}\ln g(x)=g'(x)/g(x)$.

**Ví dụ.** Nếu $p(\theta)>0$, đạo hàm log-likelihood là $\frac{d}{d\theta}\ln p(\theta)=p'(\theta)/p(\theta)$. Tính toán log giúp tích nhiều xác suất chuyển thành tổng, thường hạn chế underflow.

**Giới hạn.** Các quy tắc trên phụ thuộc miền xác định và tính khả vi. Không thể thay $\ln0$ bằng một số thực hữu hạn.

## 4.5. Tích phân và diện tích tích lũy

**Ý nghĩa.** Đạo hàm mô tả tốc độ thay đổi; tích phân xác định mô tả lượng tích lũy. Nếu $f(x)\ge0$ trên $[a,b]$, $\int_a^bf(x)\,dx$ là diện tích dưới đồ thị theo nghĩa hình học.

**Định lý cơ bản của giải tích, dạng thường dùng.** Nếu $F'(x)=f(x)$ trên khoảng và các điều kiện thích hợp được thỏa, thì

$$\int_a^b f(x)\,dx=F(b)-F(a).$$

**Ví dụ.** Vì $(x^2/2)'=x$, $\int_0^2x\,dx=[x^2/2]_0^2=2$.

**Liên hệ AI.** Xác suất của biến liên tục trên một khoảng là tích phân của hàm mật độ; kỳ vọng liên tục cũng có dạng tích phân.

## 4.6. Khai triển Taylor và xấp xỉ cục bộ

Với hàm đủ trơn gần $a$, khai triển Taylor bậc hai là

$$f(a+h)\approx f(a)+f'(a)h+\frac12 f''(a)h^2.$$

Công thức đầy đủ có số dư; mức chính xác phụ thuộc độ lớn $h$ và tính trơn. Nếu chỉ lấy bậc một, $f(a+h)\approx f(a)+f'(a)h$, đó là phép tuyến tính hóa tại $a$.

**Ví dụ.** $e^h\approx1+h$ khi $|h|$ nhỏ. Với $h=0{,}01$ thì gần 1,01; đây là xấp xỉ chứ không phải đẳng thức.

**Liên hệ AI.** Gradient Descent dùng biến thiên bậc một để chọn hướng giảm loss; phương pháp Newton dùng thông tin đạo hàm bậc hai.

# Chương 5. Đại số tuyến tính và biểu diễn dữ liệu

## 5.1. Vector, chiều và ý nghĩa hình học

Vector trong $\mathbb R^n$ là bộ $n$ số $(x_1,\ldots,x_n)$. Trong không gian Euclid, vector có độ dài và hướng. Hai vector cộng theo từng tọa độ; nhân vô hướng $c\mathbf x$ nhân mọi tọa độ với $c$.

**Ví dụ.** $\mathbf x=(2,3)$, $\mathbf y=(-1,4)$ thì $\mathbf x+\mathbf y=(1,7)$ và $2\mathbf x=(4,6)$.

**Liên hệ AI.** Một ảnh màu kích thước $H\times W\times3$ có thể làm phẳng thành vector gồm $3HW$ số, nhưng phép làm phẳng đánh mất cấu trúc không gian nếu mô hình không tận dụng hình dạng ảnh.

## 5.2. Tích vô hướng, độ dài và góc

Với $\mathbf x,\mathbf y\in\mathbb R^n$, tích vô hướng là

$$\mathbf x\cdot\mathbf y=\sum_{i=1}^n x_iy_i.$$

Chuẩn Euclid $\|\mathbf x\|_2=\sqrt{\sum_i x_i^2}$. Với hai vector khác 0,

$$\cos\theta=\frac{\mathbf x\cdot\mathbf y}{\|\mathbf x\|_2\|\mathbf y\|_2}.$$

**Ví dụ.** $(1,0)\cdot(0,1)=0$, hai vector vuông góc. $(1,2)\cdot(3,4)=11$.

**Lập luận.** Tích vô hướng đo mức đồng hướng theo nghĩa hình học khi dùng chuẩn Euclid. Giá trị bằng 0 không nói hai mẫu dữ liệu “không liên quan” theo mọi tiêu chí thống kê.

**Liên hệ AI.** Cosine similarity được dùng khi so sánh embedding; khác biệt độ lớn vector không ảnh hưởng cosine nếu cả hai vector được nhân với hệ số dương.

## 5.3. Bất đẳng thức Cauchy–Schwarz và hệ quả

**Định lý.** Với $\mathbf x,\mathbf y\in\mathbb R^n$,

$$|\mathbf x\cdot\mathbf y|\le\|\mathbf x\|_2\,\|\mathbf y\|_2.$$

**Phác thảo chứng minh.** Với $\mathbf y\ne0$ và mọi $t\in\mathbb R$, $\|\mathbf x-t\mathbf y\|_2^2\ge0$. Khai triển được tam thức bậc hai theo $t$: $\|\mathbf y\|^2t^2-2(\mathbf x\cdot\mathbf y)t+\|\mathbf x\|^2\ge0$ với mọi $t$. Do đó biệt thức $\Delta\le0$, tức $(\mathbf x\cdot\mathbf y)^2\le\|\mathbf x\|^2\|\mathbf y\|^2$. Lấy căn hai vế được kết luận; trường hợp $\mathbf y=0$ hiển nhiên.

**Hệ quả.** $-1\le\cos\theta\le1$. Vì vậy cosine similarity luôn nằm trong đoạn $[-1,1]$ với hai vector khác 0.

## 5.4. Ma trận, kích thước và phép nhân

Ma trận $A\in\mathbb R^{m\times n}$ có $m$ hàng và $n$ cột. Phép nhân $A\mathbf x$ chỉ hợp lệ khi $\mathbf x\in\mathbb R^n$; kết quả thuộc $\mathbb R^m$.

$$y_i=(A\mathbf x)_i=\sum_{j=1}^nA_{ij}x_j.$$

Nếu $A$ có kích thước $m\times n$ và $B$ có kích thước $n\times p$, thì $AB$ có kích thước $m\times p$. Thông thường $AB\ne BA$; nhiều khi $BA$ thậm chí không xác định.

**Ví dụ.** $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ và $\mathbf x=\begin{bmatrix}5\\6\end{bmatrix}$ thì $A\mathbf x=\begin{bmatrix}17\\39\end{bmatrix}$.

**Liên hệ AI.** Một minibatch $X$ gồm $B$ mẫu với $d$ đặc trưng có shape $B\times d$; trọng số $W$ shape $d\times k$; kết quả $XW$ shape $B\times k$.

## 5.5. Chuyển vị, ma trận đơn vị và nghịch đảo

Chuyển vị $A^T$ đổi hàng thành cột. Ma trận đơn vị $I$ thỏa $I\mathbf x=\mathbf x$. Ma trận vuông $A$ khả nghịch nếu tồn tại $A^{-1}$ với $AA^{-1}=A^{-1}A=I$.

**Ví dụ.** $A=\begin{bmatrix}1&0\\0&2\end{bmatrix}$ có nghịch đảo $\begin{bmatrix}1&0\\0&1/2\end{bmatrix}$. Còn ma trận $\begin{bmatrix}1&2\\2&4\end{bmatrix}$ không khả nghịch vì hàng thứ hai gấp đôi hàng thứ nhất.

**Giới hạn.** Không phải ma trận nào cũng có nghịch đảo. Khi giải bài toán hồi quy, không nên mặc định tính nghịch đảo trực tiếp là cách ổn định nhất; các thuật toán QR/SVD thường thích hợp hơn.

## 5.6. Độc lập tuyến tính, hạng và khả năng biểu diễn

Các vector $\mathbf v_1,\ldots,\mathbf v_k$ **độc lập tuyến tính** nếu $c_1\mathbf v_1+\cdots+c_k\mathbf v_k=0$ chỉ khi mọi $c_i=0$. Nếu có tổ hợp khác 0 bằng vector 0 thì chúng phụ thuộc tuyến tính.

**Ví dụ.** $(1,0)$ và $(0,1)$ độc lập. $(1,2)$ và $(2,4)$ phụ thuộc vì vector thứ hai bằng 2 lần vector thứ nhất. Hạng của ma trận là số chiều không gian cột (cũng bằng số chiều không gian hàng).

**Liên hệ AI.** Hai đặc trưng trùng lặp hoàn toàn tạo phụ thuộc tuyến tính; các phương pháp hồi quy không điều chuẩn có thể không có bộ hệ số duy nhất, dù dự đoán trên không gian dữ liệu vẫn có thể xác định.

## 5.7. Trị riêng, vector riêng và PCA

Với ma trận vuông $A$, vector khác 0 $\mathbf v$ là **vector riêng** ứng với **trị riêng** $\lambda$ nếu $A\mathbf v=\lambda\mathbf v$. Nghĩa hình học: theo hướng $\mathbf v$, phép biến đổi chỉ co giãn hoặc đảo chiều.

**Ví dụ.** $A=\mathrm{diag}(3,1)$: trục $x$ có trị riêng 3, trục $y$ có trị riêng 1.

**PCA.** Với dữ liệu đã trừ trung bình, PCA chọn các hướng trực chuẩn có phương sai lớn nhất. Các hướng này là vector riêng của ma trận hiệp phương sai (trong trường hợp thông thường); trị riêng tương ứng thể hiện lượng phương sai trên mỗi hướng.

**Giới hạn.** Phương sai lớn không đồng nghĩa đặc trưng quan trọng nhất cho dự đoán. PCA là phương pháp không giám sát và nhạy với tỷ lệ đặc trưng.

# Chương 6. Giải tích nhiều biến và tối ưu hóa

## 6.1. Đạo hàm riêng và gradient

Cho hàm $f(x_1,\ldots,x_n)$. Đạo hàm riêng $\partial f/\partial x_i$ đo biến thiên theo biến $x_i$ khi các biến khác giữ nguyên. Gradient là vector các đạo hàm riêng:

$$\nabla f=(\partial f/\partial x_1,\ldots,\partial f/\partial x_n).$$

**Ví dụ.** $f(x,y)=x^2+3xy+y^2$. Ta có $\partial f/\partial x=2x+3y$, $\partial f/\partial y=3x+2y$. Tại $(1,2)$, $\nabla f=(8,7)$.

**Ý nghĩa.** Theo xấp xỉ bậc nhất, khi bước $\Delta\mathbf x$ nhỏ, $\Delta f\approx\nabla f\cdot\Delta\mathbf x$. Gradient chỉ đúng hướng tăng nhanh nhất theo chuẩn Euclid tại điểm khả vi, không bảo đảm tăng trên bước lớn tùy ý.

## 6.2. Jacobian, Hessian và hình dạng biến đổi

Với hàm vector $\mathbf f:\mathbb R^n\to\mathbb R^m$, **Jacobian** $J$ là ma trận $m\times n$ với $J_{ij}=\partial f_i/\partial x_j$. Với hàm vô hướng $f$, **Hessian** $H$ gồm các đạo hàm riêng bậc hai $H_{ij}=\partial^2f/\partial x_i\partial x_j$.

**Ví dụ.** $f(x,y)=x^2+2y^2$ có $\nabla f=(2x,4y)$ và $H=\begin{bmatrix}2&0\\0&4\end{bmatrix}$. Hessian dương xác định, nên $f$ lồi nghiêm ngặt; cực tiểu duy nhất tại $(0,0)$.

**Liên hệ AI.** Jacobian mô tả ảnh hưởng đầu vào lên nhiều đầu ra; Hessian mô tả độ cong loss. Nhiều mô hình lớn không tính Hessian đầy đủ do chi phí lưu trữ và tính toán cao.

## 6.3. Cực trị, điểm dừng và tính lồi

Nếu $f$ khả vi và đạt cực trị cục bộ ở điểm trong miền, điều kiện cần là $\nabla f=0$. Đây **không phải điều kiện đủ**: $f(x)=x^3$ có đạo hàm bằng 0 tại 0 nhưng không có cực tiểu hay cực đại tại đó.

**Định nghĩa.** Hàm $f$ lồi trên miền lồi nếu với $0\le t\le1$,

$$f(tx+(1-t)y)\le tf(x)+(1-t)f(y).$$

Với hàm lồi khả vi, mọi điểm có gradient bằng 0 là cực tiểu toàn cục. Với hàm lồi nghiêm ngặt, cực tiểu (nếu tồn tại) là duy nhất.

**Liên hệ AI.** Hồi quy tuyến tính bình phương tối thiểu có hàm loss lồi theo hệ số. Neural network nhiều lớp nhìn chung có loss không lồi theo trọng số.

## 6.4. Gradient Descent: suy ra quy tắc cập nhật

Mục tiêu: tìm tham số $\theta$ làm giảm hàm khả vi $L(\theta)$. Ở gần $\theta$, xấp xỉ bậc nhất là

$$L(\theta+\Delta\theta)\approx L(\theta)+\nabla L(\theta)^T\Delta\theta.$$

Nếu chọn $\Delta\theta=-\eta\nabla L(\theta)$ với $\eta>0$, phần tuyến tính thay đổi bằng $-\eta\|\nabla L\|^2\le0$. Đó là cơ sở để cập nhật

$$\theta_{t+1}=\theta_t-\eta\nabla L(\theta_t).$$

**Giới hạn quan trọng.** Lập luận trên chỉ dựa xấp xỉ khi bước đủ nhỏ. Gradient Descent **không bảo đảm loss giảm ở mọi bước** nếu learning rate quá lớn, gradient sai hoặc hàm có tính chất bất lợi.

**Ví dụ tính tay.** $L(w)=(w-3)^2$, $L'(w)=2(w-3)$. Từ $w_0=0$, chọn $\eta=0{,}25$: $w_1=0-0{,}25(-6)=1{,}5$. Loss giảm từ 9 xuống 2,25.

## 6.5. Chứng minh giảm loss với hàm trơn

**Mệnh đề có điều kiện.** Giả sử gradient của $L$ là $\beta$-Lipschitz (thường gọi *$\beta$-smooth*). Khi đó với mọi $x,y$:

$$L(y)\le L(x)+\nabla L(x)^T(y-x)+\frac\beta2\|y-x\|^2.$$

Thay $y=x-\eta\nabla L(x)$ ta được

$$L(y)\le L(x)-\eta\left(1-\frac{\beta\eta}{2}\right)\|\nabla L(x)\|^2.$$

Vì vậy, nếu $0<\eta\le1/\beta$, vế trừ là không âm và loss không tăng. Đây là một **bảo đảm có giả thiết**, không áp dụng nguyên xi cho mọi mạng neural hay minibatch ngẫu nhiên.

**Ứng dụng.** Điều kiện về learning rate giúp giải thích vì sao một số bước tối ưu quá lớn gây dao động hoặc phân kỳ.

# Chương 7. Xác suất: mô tả bất định

## 7.1. Không gian mẫu và biến cố

**Định nghĩa.** Không gian mẫu $\Omega$ gồm mọi kết quả có thể của thí nghiệm; biến cố $A$ là tập con của $\Omega$. Xác suất $P$ thỏa $P(A)\ge0$, $P(\Omega)=1$ và cộng được trên các biến cố rời nhau.

**Ví dụ.** Tung đồng xu công bằng: $\Omega=\{\text{sấp},\text{ngửa}\}$, $P(\text{ngửa})=1/2$. Mô hình “công bằng” là giả thiết về cơ chế sinh dữ liệu, không thể tự xác nhận chỉ từ một vài lần tung.

**Chú ý.** Xác suất là tính chất của mô hình và thông tin được giả định; dự đoán xác suất từ mô hình ML có thể **chưa được hiệu chuẩn** (calibrated).

## 7.2. Xác suất có điều kiện và sự độc lập

Nếu $P(B)>0$, xác suất có điều kiện

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}.$$

Suy ra quy tắc nhân: $P(A\cap B)=P(A\mid B)P(B)$. Hai biến cố độc lập nếu $P(A\cap B)=P(A)P(B)$; khi $P(B)>0$ điều này tương đương $P(A\mid B)=P(A)$.

**Ví dụ.** Rút một lá bài chuẩn, $A$ là “lá đỏ”, $B$ là “lá cơ”. Khi biết lá cơ thì chắc chắn lá đỏ: $P(A\mid B)=1$, khác $P(A)=1/2$. Do đó hai biến cố không độc lập.

**Liên hệ AI.** Tính độc lập giữa các đặc trưng là giả thiết trong Naive Bayes; tên “naive” nhắc rằng giả thiết này thường không đúng hoàn toàn ngoài đời.

## 7.3. Định lý Bayes và tỷ lệ nền

Từ quy tắc nhân hai chiều,

$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)},\quad P(B)>0.$$

**Ví dụ kiểm tra cảnh báo.** Giả sử 1% sản phẩm thật sự lỗi. Bộ phát hiện có độ nhạy 90% và tỷ lệ báo giả 5%. Xác suất lỗi khi báo động là

$$P(\text{lỗi}\mid\text{báo})=\frac{0.90\cdot0.01}{0.90\cdot0.01+0.05\cdot0.99}\approx0.154.$$

Dù độ nhạy cao, chỉ khoảng 15,4% sản phẩm bị cảnh báo thực sự lỗi trong mô hình giả định này. **Nguyên nhân** là tỷ lệ nền lỗi thấp.

**Liên hệ AI.** Trong phát hiện gian lận hoặc bệnh hiếm, cần quan tâm precision và tỷ lệ nền, không chỉ sensitivity/recall.

## 7.4. Biến ngẫu nhiên, kỳ vọng và phương sai

Một biến ngẫu nhiên $X$ gán một số cho mỗi kết quả. Nếu rời rạc với xác suất $p_i=P(X=x_i)$, kỳ vọng

$$\mathbb E[X]=\sum_i x_ip_i.$$

Phương sai đo phân tán quanh kỳ vọng:

$$\operatorname{Var}(X)=\mathbb E[(X-\mu)^2]=\mathbb E[X^2]-\mu^2,\quad\mu=\mathbb E[X].$$

**Chứng minh đẳng thức.** Khai triển $(X-\mu)^2=X^2-2\mu X+\mu^2$, lấy kỳ vọng và dùng $\mathbb E[X]=\mu$ thu được $\mathbb E[X^2]-2\mu^2+\mu^2$.

**Ví dụ.** $X$ nhận 0 hoặc 1 với xác suất bằng nhau: $\mathbb E[X]=1/2$, $\operatorname{Var}(X)=1/4$.

## 7.5. Một số phân phối cơ bản

**Bernoulli($p$).** Biến $X\in\{0,1\}$ với $P(X=1)=p$, $P(X=0)=1-p$. Khi đó $\mathbb E[X]=p$ và $\operatorname{Var}(X)=p(1-p)$.

**Binomial($n,p$).** Đếm số thành công trong $n$ phép thử Bernoulli độc lập và cùng xác suất: $P(X=k)=\binom nk p^k(1-p)^{n-k}$.

**Normal($\mu,\sigma^2$).** Biến liên tục với mật độ hình chuông, kỳ vọng $\mu$ và phương sai $\sigma^2$. Mật độ không phải xác suất tại một điểm; với biến liên tục thông thường, $P(X=a)=0$, còn xác suất khoảng được tính bằng tích phân.

**Liên hệ AI.** Phân phối Bernoulli thường mô hình hóa nhãn nhị phân; phân phối chuẩn được dùng trong một số giả thiết nhiễu và mô hình xác suất. Không phải mọi dữ liệu thực đều phân phối chuẩn.

# Chương 8. Thống kê, lấy mẫu và đánh giá bằng chứng

## 8.1. Tổng thể, mẫu và ước lượng

**Tổng thể** là tập đối tượng mà ta muốn suy luận; **mẫu** là tập đối tượng đã quan sát. Trung bình mẫu $\bar x=(1/n)\sum_i x_i$ ước lượng kỳ vọng tổng thể $\mu$ khi lấy mẫu phù hợp.

Phương sai mẫu thường dùng

$$s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2\quad(n\ge2).$$

Mẫu số $n-1$ liên quan điều chỉnh độ lệch khi ước lượng phương sai tổng thể dưới các giả thiết lấy mẫu độc lập, cùng phân phối và phương sai hữu hạn.

**Lưu ý.** Một mẫu rất lớn nhưng chọn lệch có thể cho kết luận kém hơn mẫu nhỏ được lấy đúng phương pháp. Số mẫu không tự sửa sai lệch chọn mẫu.

## 8.2. Luật số lớn và sự hội tụ

**Ý tưởng.** Khi các biến ngẫu nhiên độc lập, cùng phân phối và có kỳ vọng hữu hạn, trung bình mẫu tiến gần kỳ vọng khi số quan sát tăng (theo một kiểu hội tụ xác suất). Đây là **luật số lớn**.

**Ví dụ.** Tung đồng xu công bằng nhiều lần, tỷ lệ ngửa thường tiến gần 1/2 khi số lần tung lớn. Luật không bảo đảm đúng 1/2 sau một số lần hữu hạn, cũng không có nghĩa các lần tung “phải bù” cho nhau.

**Liên hệ AI.** Loss trung bình trên một minibatch có thể là ước lượng nhiễu của loss toàn tập. Minibatch lớn thường giảm phương sai ước lượng trong các điều kiện quen thuộc, nhưng không bảo đảm tối ưu nhanh hơn theo thời gian thực.

## 8.3. Khoảng tin cậy và diễn giải đúng

Khoảng tin cậy 95% được xây bằng một thủ tục mà, dưới giả thiết của mô hình, **nếu lặp lại quy trình lấy mẫu rất nhiều lần thì khoảng 95% các khoảng tạo ra sẽ bao chứa tham số thật**. Không nên diễn giải trực tiếp “tham số cố định có 95% xác suất nằm trong khoảng đã tính” theo xác suất học cổ điển.

**Ví dụ gần đúng.** Nếu trung bình mẫu $\bar x$ có sai số chuẩn $SE$ và phân phối lấy mẫu gần chuẩn, khoảng xấp xỉ $\bar x\pm1.96SE$. Điều kiện phân phối và cách ước lượng $SE$ phải phù hợp; không áp dụng máy móc cho mẫu nhỏ, dữ liệu lệch mạnh hoặc có phụ thuộc.

**Liên hệ AI.** Khi so sánh accuracy của hai mô hình, chênh lệch nhỏ có thể xuất phát từ biến động mẫu hoặc lần huấn luyện, cần đánh giá sự không chắc chắn.

## 8.4. Tương quan không phải nhân quả

Hệ số tương quan Pearson đo mức liên hệ tuyến tính:

$$\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y},\qquad\sigma_X,\sigma_Y>0.$$

$\rho$ gần 0 chỉ nói liên hệ tuyến tính yếu, không loại trừ quan hệ phi tuyến. Và tương quan mạnh không chứng minh $X$ gây ra $Y$: có thể tồn tại biến gây nhiễu, chọn mẫu lệch hoặc quan hệ ngược.

**Liên hệ AI.** Một mô hình dự đoán tốt nhờ đặc trưng “rò rỉ tương lai” không đồng nghĩa nó có khả năng dự đoán thực tế khi triển khai. Cần xác định mốc thời gian dữ liệu và cơ chế sinh đặc trưng.

# Chương 9. Lý thuyết thông tin và hàm mất mát

## 9.1. Entropy: mức bất định của phân phối

Với phân phối rời rạc $p=(p_1,\ldots,p_K)$, entropy Shannon cơ số 2 là

$$H(p)=-\sum_{i=1}^K p_i\log_2p_i,$$

quy ước $0\log 0=0$ theo giới hạn. Đơn vị là *bit* khi log cơ số 2; dùng $\ln$ thì đơn vị là *nat*.

**Ví dụ.** Đồng xu công bằng có $H=-2(1/2\log_2(1/2))=1$ bit. Đồng xu luôn ngửa có entropy 0: không còn bất định về kết quả trong mô hình.

**Liên hệ AI.** Entropy thường được dùng để đo độ hỗn loạn phân lớp trong cây quyết định và lượng bất định của phân phối dự đoán, nhưng entropy thấp không chứng minh mô hình đúng.

## 9.2. Cross-entropy và KL divergence

Với phân phối thật $p$ và phân phối dự đoán $q$ (yêu cầu $q_i>0$ khi $p_i>0$), cross-entropy dùng log tự nhiên:

$$H(p,q)=-\sum_i p_i\ln q_i.$$

KL divergence là $D_{KL}(p\|q)=\sum_i p_i\ln(p_i/q_i)$. Có hệ thức

$$H(p,q)=H(p)+D_{KL}(p\|q),$$

trong đó $H(p)=-\sum_ip_i\ln p_i$ tính bằng nat. Vì $D_{KL}\ge0$, cross-entropy nhỏ nhất (trên các phân phối $q$ hợp lệ) khi $q=p$.

**Giải thích vì sao $D_{KL}\ge0$.** Từ bất đẳng thức $\ln t\le t-1$ với $t>0$, thay $t=q_i/p_i$ cho $p_i>0$ và cộng theo trọng số $p_i$, ta được $\sum_i p_i\ln(q_i/p_i)\le\sum_i(q_i-p_i)\le0$. Đổi dấu suy ra KL không âm. Dấu bằng đạt khi $q=p$ trên miền hỗ trợ phù hợp.

## 9.3. Binary cross-entropy và ý nghĩa nhãn

Với nhãn $y\in\{0,1\}$ và xác suất dự đoán $0<p<1$,

$$\ell(y,p)=-y\ln p-(1-y)\ln(1-p).$$

Nếu $y=1$ thì $\ell=-\ln p$; khi $p\to0$, loss tăng không giới hạn. Nếu $y=0$ thì $\ell=-\ln(1-p)$; khi $p\to1$, loss tăng mạnh.

**Ví dụ.** Nhãn thật $y=1$: dự đoán $p=0{,}9$ cho loss khoảng 0,105; dự đoán $p=0{,}1$ cho loss khoảng 2,303. Hàm loss phạt nặng dự đoán sai nhưng rất tự tin.

**Liên hệ AI.** Trong thực thi số học nên dùng các phép loss ổn định nhận *logits* trực tiếp thay vì tự tính $\ln(0)$ sau bước làm tròn.

# Chương 10. Toán số trên máy tính

## 10.1. Số thực lý tưởng khác với floating point

Máy tính lưu số thực hữu hạn bằng số bit cố định; nhiều phân số thập phân không có biểu diễn hữu hạn trong hệ nhị phân. Bởi vậy giá trị 0,1 trong định dạng binary floating point thông dụng chỉ là một số gần 0,1.

**Lập luận.** Một số hữu tỉ có biểu diễn hữu hạn trong hệ nhị phân chỉ khi ở dạng rút gọn, mẫu số là lũy thừa của 2. Phân số $1/10$ có mẫu $10=2\cdot5$, còn thừa thừa số 5 nên không thể biểu diễn nhị phân hữu hạn.

**Hệ quả.** Không nên mặc định phép cộng/trừ số thực có tính kết hợp chính xác ở độ dài bit hữu hạn: $(a+b)+c$ và $a+(b+c)$ có thể cho kết quả khác vì làm tròn.

## 10.2. Sai số tuyệt đối, tương đối và số điều kiện

Nếu $x$ là giá trị thật và $\hat x$ là giá trị gần đúng, sai số tuyệt đối $|\hat x-x|$, sai số tương đối $|\hat x-x|/|x|$ khi $x\ne0$.

**Ví dụ.** Gần đúng 100 bằng 101 có sai số tuyệt đối 1, tương đối 1%. Gần đúng 0,01 bằng 1,01 cũng sai số tuyệt đối 1 nhưng sai số tương đối 10.000%.

Một bài toán **điều kiện kém** khi thay đổi rất nhỏ ở đầu vào có thể làm đầu ra thay đổi lớn. **Ổn định số** là tính chất của thuật toán kiểm soát lỗi làm tròn. Hai ý này khác nhau: bài toán điều kiện kém có thể khiến mọi thuật toán hữu hạn gặp khó.

## 10.3. Tràn số, underflow và log-sum-exp

Khi tính $e^{x_i}$ với $x_i$ lớn, có thể tràn số. Với $x_i$ rất âm, có thể underflow về 0. Đặt $m=\max_i x_i$, ta có đẳng thức đại số:

$$\ln\sum_i e^{x_i}=m+\ln\sum_i e^{x_i-m}.$$

**Giải thích.** Tách $e^m$ khỏi tổng: $\sum_i e^{x_i}=e^m\sum_i e^{x_i-m}$. Lấy $\ln$ và sử dụng $\ln(ab)=\ln a+\ln b$. Vì $x_i-m\le0$, mỗi $e^{x_i-m}\le1$, giảm nguy cơ tràn số trong bước tính mũ.

**Liên hệ AI.** Softmax và cross-entropy dùng cùng ý tưởng ổn định. Công thức đúng trên số thực không có nghĩa mọi phép tính floating point đều hoàn toàn chính xác.

# Chương 11. Từ toán đến Machine Learning

## 11.1. Mẫu, đặc trưng, nhãn và tham số

Giả sử có $n$ mẫu, mỗi mẫu $\mathbf x_i\in\mathbb R^d$, nhãn $y_i$. Ma trận dữ liệu $X$ có shape $n\times d$, vector nhãn $\mathbf y$ có độ dài $n$. Mô hình $f_\theta$ nhận đặc trưng $\mathbf x$ và đưa dự đoán $\hat y$.

**Khái niệm.** *Tham số* là giá trị mô hình học từ dữ liệu, như vector trọng số. *Siêu tham số* là lựa chọn điều khiển cách mô hình được xây dựng/huấn luyện, như learning rate hoặc số tầng. Mục tiêu là học quy luật khái quát hóa, không chỉ ghi nhớ tập huấn luyện.

**Liên hệ thiết kế.** Trước khi chọn thuật toán, cần xác định đối tượng dự đoán, mốc thời gian, đơn vị nhãn, chi phí sai lầm và phương pháp đánh giá.

## 11.2. Hồi quy tuyến tính và least squares

Mô hình hồi quy affine một chiều là $\hat y=wx+b$. Với dữ liệu $(x_i,y_i)$, hàm bình phương trung bình:

$$L(w,b)=\frac1n\sum_{i=1}^n(wx_i+b-y_i)^2.$$

**Giải thích.** Sai số $e_i=\hat y_i-y_i$ có thể dương hoặc âm. Bình phương khiến hai phía đều góp phần không âm và phạt mạnh sai số lớn; nhưng cũng khiến mô hình nhạy với outlier.

**Ví dụ.** Nếu $x=(0,1)$ và $y=(1,3)$, đường thẳng $\hat y=2x+1$ khớp hoàn toàn cả hai điểm, nên loss bằng 0. Hai điểm không bảo đảm mô hình đúng cho dữ liệu mới.

## 11.3. Ridge regularization và sự đánh đổi

Ridge thêm bình phương độ lớn tham số vào loss:

$$L_{\mathrm{ridge}}(w)=\frac1n\sum_i(\hat y_i-y_i)^2+\lambda\|w\|_2^2,\quad\lambda\ge0.$$

**Ý nghĩa.** Tăng $\lambda$ gây áp lực thu nhỏ trọng số, có thể giảm phương sai mô hình và hạn chế overfit, nhưng nếu quá lớn có thể underfit. Tùy định nghĩa, hệ số phạt có thể có các hằng số 1/2 hoặc 1/n khác nhau.

**Liên hệ AI.** Regularization không phải phép “chứng minh mô hình đúng”; đó là đưa thêm thiên lệch có chủ đích để hy vọng cải thiện tổng quát hóa.

## 11.4. Logistic Regression và sigmoid

Với bài toán nhị phân, mô hình xác suất thường dùng

$$p(y=1\mid\mathbf x)=\sigma(w^T\mathbf x+b),\quad \sigma(z)=\frac1{1+e^{-z}}.$$

Sigmoid biến mọi số thực thành giá trị trong $(0,1)$. Đạo hàm của sigmoid:

$$\sigma'(z)=\sigma(z)(1-\sigma(z)).$$

**Chứng minh.** $\sigma(z)=(1+e^{-z})^{-1}$; dùng quy tắc dây chuyền được $\sigma'(z)=e^{-z}/(1+e^{-z})^2$. Vì $1-\sigma(z)=e^{-z}/(1+e^{-z})$, biểu thức bằng $\sigma(z)(1-\sigma(z))$.

**Liên hệ AI.** Logistic Regression là mô hình tuyến tính trên *log-odds*, không phải hàm dự đoán tuyến tính của xác suất.

## 11.5. Ma trận nhầm lẫn và metric phân loại

Với phân loại nhị phân, bốn ô của confusion matrix là TP (dương đúng), FP (dương sai), FN (âm sai), TN (âm đúng). Khi mẫu số dương:

$$\mathrm{Precision}=\frac{TP}{TP+FP},\qquad \mathrm{Recall}=\frac{TP}{TP+FN}.$$

$$F_1=\frac{2PR}{P+R}\quad(P+R>0).$$

**Ví dụ.** Nếu TP=8, FP=2, FN=4 thì precision = 8/10 = 0,8, recall = 8/12 \(\approx0,667\). F1 \(\approx0,727\).

**Giới hạn.** Metric có thể không xác định khi mẫu số 0; thư viện có quy tắc xử lý riêng. Accuracy dễ gây ngộ nhận khi lớp dương rất hiếm.

# Chương 12. Deep Learning: đạo hàm chạy qua mạng nhiều lớp

## 12.1. Neuron nhân tạo và hàm kích hoạt

Một neuron điển hình tính $z=w^T\mathbf x+b$ rồi trả $a=\phi(z)$, trong đó $\phi$ là hàm kích hoạt. Nếu bỏ mọi activation phi tuyến giữa các lớp affine, hợp của nhiều lớp vẫn chỉ là một phép affine.

**Chứng minh.** Hai lớp $f_1(x)=W_1x+b_1$ và $f_2(h)=W_2h+b_2$ cho $f_2(f_1(x))=W_2W_1x+(W_2b_1+b_2)$; đó là một phép affine. Vì vậy phi tuyến đóng vai trò quan trọng trong năng lực biểu diễn của mạng nhiều lớp.

**Liên hệ AI.** ReLU $\phi(z)=\max(0,z)$ là một lựa chọn thường gặp. Nó không khả vi tại 0 theo nghĩa đạo hàm cổ điển; các framework sử dụng quy ước đạo hàm dưới gradient tại điểm này.

## 12.2. Lan truyền thuận và loss

Với mạng hai lớp, có thể viết

$$h=\phi(W_1x+b_1),\quad \hat y=g(W_2h+b_2),\quad L=\ell(\hat y,y).$$

*Lan truyền thuận* (forward pass) tính từng biến trung gian từ đầu vào đến loss. Mỗi phép nhân ma trận đòi hỏi kích thước khớp nhau. Có thể ghi theo chuỗi $x\to z_1\to h\to z_2\to\hat y\to L$ để theo dõi phép đạo hàm.

**Điểm quan trọng.** Loss là thước đo theo mục tiêu và giả định định nghĩa trước; giá trị nhỏ trên tập huấn luyện không tự chứng minh tính tổng quát hóa.

## 12.3. Backpropagation: quy tắc dây chuyền có tổ chức

Giả sử $z=wx+b$, $a=\phi(z)$ và loss $L(a)$. Quy tắc dây chuyền cho

$$\frac{\partial L}{\partial w}=\frac{\partial L}{\partial a}\frac{\partial a}{\partial z}\frac{\partial z}{\partial w}=\frac{\partial L}{\partial a}\phi'(z)x.$$

**Ví dụ.** Nếu $\phi$ là hàm đồng nhất và $L=(a-y)^2/2$, thì $\partial L/\partial a=a-y$. Suy ra $\partial L/\partial w=(wx+b-y)x$ và $\partial L/\partial b=wx+b-y$.

**Ý nghĩa.** Backpropagation không phải thuật toán tối ưu độc lập: nó *tính gradient hiệu quả*. Optimizer như SGD hoặc Adam sử dụng gradient đó để cập nhật tham số.

## 12.4. Vanishing, exploding gradients và chuẩn hóa

Trong mạng sâu, gradient gồm tích của nhiều đạo hàm/Jacobian. Nếu nhiều hệ số có độ lớn nhỏ hơn 1, tích có thể rất nhỏ; nếu lớn hơn 1, có thể rất lớn. Đây là trực giác của **vanishing/exploding gradients**.

**Giới hạn của trực giác.** Trong mạng thật còn có hình học ma trận, trị riêng/singular values, skip connections, chuẩn hóa và optimizer; không thể chỉ nhìn một hệ số vô hướng để kết luận.

**Liên hệ AI.** Khởi tạo trọng số, activation phù hợp, normalization và residual connections đều góp phần cải thiện quá trình tối ưu ở những cấu hình nhất định.

## 12.5. Bias–variance và overfitting

*Bias* là sai lệch có hệ thống từ giả thiết mô hình; *variance* là mức nhạy của kết quả học với thay đổi dữ liệu huấn luyện. Trong thiết lập bình phương sai số, có một phân rã kinh điển (theo giả thiết nhiễu và kỳ vọng phù hợp):

$$\mathbb E[(\hat f(x)-y)^2]=\mathrm{Bias}(\hat f(x))^2+\mathrm{Var}(\hat f(x))+\sigma_\varepsilon^2.$$

**Ý nghĩa.** Mô hình quá đơn giản có thể bias cao, mô hình rất linh hoạt có thể variance cao nếu dữ liệu ít. Nhưng đây là khung phân tích, không phải quy luật rằng mọi mô hình lớn đều overfit.

**Liên hệ AI.** Cần đánh giá dữ liệu chưa thấy và tránh dùng tập test lặp đi lặp lại để chỉnh mô hình.

# Chương 13. Toán học cho Computer Vision

## 13.1. Ảnh số là mảng nhiều chiều

Một ảnh xám có thể được biểu diễn bằng ma trận $H\times W$; ảnh RGB thường có tensor $H\times W\times3$ (tùy quy ước trục của thư viện). Mỗi phần tử là giá trị cường độ hoặc màu sắc đã lượng tử hóa/chuẩn hóa.

**Ví dụ.** Ảnh RGB $224\times224$ có $224\cdot224\cdot3=150.528$ giá trị kênh. Con số này là số phần tử, **không phải** kích thước byte; byte phụ thuộc kiểu dữ liệu.

**Liên hệ AI.** Việc hoán đổi chiều kênh (channels-first/channels-last) làm thay đổi cách dữ liệu được diễn giải dù tổng số phần tử không đổi.

## 13.2. Convolution, cross-correlation và bộ lọc

Trong nhiều thư viện deep learning, thao tác được gọi là “convolution” thực chất tính **cross-correlation** (không đảo kernel). Với ảnh xám $X$ và kernel $K$ kích thước $k_h\times k_w$:

$$Y_{i,j}=\sum_{u=0}^{k_h-1}\sum_{v=0}^{k_w-1}X_{i+u,j+v}K_{u,v},$$

trong trường hợp stride 1, không padding và các chỉ số hợp lệ. Convolution toán học đảo chiều kernel trước khi trượt; mô hình học máy có thể học được trọng số tương ứng nên tên gọi thực hành vẫn phổ biến.

**Ví dụ.** Kernel trung bình $2\times2$ có bốn phần tử 1/4. Áp lên cửa sổ $\begin{bmatrix}1&3\\5&7\end{bmatrix}$ cho kết quả $(1+3+5+7)/4=4$.

## 13.3. Padding, stride và kích thước đầu ra

Với kích thước đầu vào $N$, kernel $K$, padding $P$ mỗi bên, dilation $D$, stride $S$, kích thước đầu ra trên một trục là

$$N_{out}=\left\lfloor\frac{N+2P-D(K-1)-1}{S}\right\rfloor+1,$$

khi các giá trị hợp lệ theo quy ước convolution thông dụng. Đây là đếm số vị trí hợp lệ của cửa sổ sau padding và dilation.

**Ví dụ.** $N=5,K=3,P=0,D=1,S=1$ cho $N_{out}=3$. Nếu $P=1$ thì $N_{out}=5$. Với ảnh hai chiều, tính riêng chiều cao và rộng.

**Liên hệ AI.** Một nhầm lẫn stride/padding có thể làm lỗi shape trước khi đến phép nhân fully connected.

## 13.4. Pooling và bất biến cục bộ

Max pooling lấy phần tử lớn nhất trong cửa sổ; average pooling lấy trung bình. Với cửa sổ $\begin{bmatrix}1&3\\5&7\end{bmatrix}$, max pooling cho 7, average pooling cho 4.

**Ý nghĩa.** Pooling làm giảm kích thước và mức nhạy với một số thay đổi vị trí nhỏ, nhưng đồng thời đánh mất thông tin không gian. “Bất biến với phép tịnh tiến” chỉ là tính chất tương đối trong cấu hình và phạm vi nhất định, không phải bất biến tuyệt đối của mọi CNN.

## 13.5. Softmax và xác suất phân lớp ảnh

Với logits $z_1,\ldots,z_K$,

$$\operatorname{softmax}(z)_i=\frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}.$$

Mỗi giá trị dương và tổng bằng 1. Nếu cộng cùng một hằng số $c$ vào mọi logit, softmax không đổi vì $e^{z_i+c}$ có cùng thừa số $e^c$ ở tử và mẫu.

**Chứng minh bất biến tịnh tiến.** $e^{z_i+c}/\sum_j e^{z_j+c}=e^ce^{z_i}/(e^c\sum_j e^{z_j})=e^{z_i}/\sum_j e^{z_j}$.

**Giới hạn.** Tổng bằng 1 không bảo đảm xác suất đã được calibration tốt. Mạng có thể rất tự tin nhưng dự đoán sai khi dữ liệu khác phân phối huấn luyện.

# Chương 14. Toán học của phép đo chất lượng và khả năng khái quát hóa

## 14.1. Train, validation và test phục vụ các vai trò khác nhau

Dữ liệu **train** dùng ước lượng tham số; **validation** dùng chọn mô hình và siêu tham số; **test** dùng ước lượng cuối cùng trên dữ liệu chưa tham gia lựa chọn. Việc xem test rồi chỉnh mô hình nhiều lần có thể khiến tập test bị sử dụng như validation và làm đánh giá lạc quan.

**Ví dụ.** Với dữ liệu ảnh của cùng một người hoặc cùng một video, chia ngẫu nhiên theo ảnh/frame có thể khiến các mẫu rất giống nhau xuất hiện ở train và test. Khi đó điểm test cao không chứng minh hệ thống hoạt động trên người/video mới.

**Giới hạn.** Chia tách phù hợp tùy cách triển khai thực tế: chia theo thời gian, theo nhóm, theo đối tượng hay theo thiết bị.

## 14.2. Kỳ vọng rủi ro và rủi ro thực nghiệm

Mục tiêu lý tưởng là cực tiểu hóa kỳ vọng loss trên phân phối dữ liệu thật $P$:

$$R(\theta)=\mathbb E_{(X,Y)\sim P}[\ell(f_\theta(X),Y)].$$

Vì không biết $P$, ta dùng trung bình loss trên mẫu huấn luyện:

$$\hat R_n(\theta)=\frac1n\sum_{i=1}^n\ell(f_\theta(x_i),y_i).$$

**Giải thích.** Hai biểu thức chỉ gần nhau dưới các giả thiết phù hợp (lấy mẫu, mức phức tạp giả thuyết, tính chất loss...). Loss train nhỏ không đủ để kết luận rủi ro thật nhỏ.

**Liên hệ AI.** Toàn bộ câu chuyện tổng quát hóa liên quan khoảng cách giữa $\hat R_n$ và $R$, cũng như cách dữ liệu thay đổi sau triển khai.

## 14.3. Precision–Recall và lựa chọn ngưỡng theo rủi ro

Với score liên tục $s(x)$, chọn ngưỡng $\tau$ để dự đoán dương khi $s(x)\ge\tau$. Hạ ngưỡng thường làm tăng số dự đoán dương; recall thường tăng hoặc không giảm, nhưng precision không nhất thiết thay đổi đơn điệu với ngưỡng trên mọi tập dữ liệu.

**Ví dụ.** Trong phát hiện khuyết tật sản xuất, FN có thể gây thiệt hại chất lượng, còn FP làm tăng chi phí kiểm tra thủ công. Chọn ngưỡng phải dựa vào tỷ lệ lỗi và chi phí hai loại sai lầm, không chỉ tối đa một metric mặc định.

## 14.4. Thang đo và so sánh mô hình công bằng

So sánh mô hình cần cùng tập đánh giá, cùng cách tiền xử lý hợp lệ, cùng định nghĩa metric, và ghi rõ độ biến thiên theo các lần chạy. Một cải thiện 0,5 điểm phần trăm có thể có giá trị hoặc chỉ là nhiễu, tùy kích thước/độ phụ thuộc của tập đánh giá.

**Chú ý.** Không gộp nhiều kết quả thành một con số nếu các mẫu bị trùng lặp hoặc chịu cùng nguồn nhiễu. Có thể phân tích theo nhóm điều kiện ánh sáng, góc chụp, loại thiết bị, mức độ khó để phát hiện vấn đề hệ thống.

# Chương 15. Bản đồ tổng hợp: học toán để đọc AI không bị mất gốc

## 15.1. Từ dữ liệu đến dự đoán

Xét bài toán nhận diện vật thể trong ảnh. Ảnh là tensor nhiều chiều (Chương 5, 13). Mô hình biến đổi qua ma trận và hàm kích hoạt (Chương 3, 5, 12). Đầu ra có thể là các logits, chuyển thành phân phối bằng softmax (Chương 9, 13). Loss so sánh dự đoán với nhãn (Chương 9, 11). Backpropagation tính gradient (Chương 4, 6, 12), optimizer cập nhật trọng số (Chương 6). Sau cùng, đánh giá trên dữ liệu độc lập (Chương 8, 14).

**Chuỗi tư duy cần nhớ:** dữ liệu $\to$ biểu diễn $\to$ hàm mô hình $\to$ dự đoán $\to$ loss $\to$ gradient $\to$ cập nhật $\to$ đánh giá.

## 15.2. Bảng liên hệ thuật ngữ, công thức và ứng dụng

- **Vector / ma trận:** phép biến đổi $Wx+b$, quy tắc shape; ứng dụng trong Dense layer và embedding.
- **Đạo hàm / gradient:** $\nabla L$, quy tắc dây chuyền; ứng dụng trong huấn luyện tham số.
- **Tích phân / xác suất:** $P(a<X<b)=\int_a^bp(x)\,dx$; ứng dụng với biến liên tục.
- **Entropy / cross-entropy:** $-\sum_i p_i\ln q_i$; ứng dụng trong loss phân loại.
- **Phương sai / thống kê:** $\mathbb E[(X-\mu)^2]$; ứng dụng khi mô tả dữ liệu và đánh giá.
- **Tích chập (convolution):** tổng có trọng số trên vùng ảnh; ứng dụng với bộ lọc và CNN.
- **Số học floating point:** làm tròn, overflow và underflow; ứng dụng trong tính toán ổn định.
- **Rủi ro tổng quát hóa:** so sánh $R(\theta)$ và $\hat R_n(\theta)$; ứng dụng trong đánh giá ngoài mẫu.

## 15.3. Checklist tự kiểm tra khi gặp một công thức mới

1. **Tên và loại đối tượng:** là số vô hướng, vector, ma trận, tensor, hàm hay xác suất?
2. **Giả thiết:** miền giá trị, độc lập, khả vi, không bằng 0, chuẩn hóa, phân phối... đã được nêu chưa?
3. **Kích thước và đơn vị:** các phép cộng/nhân có phù hợp shape và đơn vị không?
4. **Bước biến đổi:** phép toán nào được dùng và vì sao hợp lệ?
5. **Ranh giới:** đây là đẳng thức, xấp xỉ, định lý có điều kiện hay kết quả thực nghiệm?
6. **Ứng dụng:** đầu vào thực tế có đáp ứng đúng những giả thiết đó không?

**Kết luận.** Thành thạo toán để học AI không có nghĩa phải thuộc mọi chứng minh; quan trọng là hiểu ký hiệu, xác định giả thiết, tự khôi phục các phép suy luận chủ chốt và biết khi nào một công thức không còn áp dụng. Sau Tập 00, nên học Tập 01 về Python cơ bản trước khi triển khai các thuật toán ML/DL.

# Phụ lục A. Từ điển ký hiệu cần nhớ

- **$\in$, $\subseteq$:** thuộc tập, là tập con.
- **$\forall$, $\exists$:** với mọi, tồn tại.
- **$\Rightarrow$, $\Leftrightarrow$:** suy ra, tương đương.
- **$\sum$, $\prod$:** phép lấy tổng, phép lấy tích.
- **$\lim$, $\int$:** giới hạn, tích phân.
- **$f'(x)$, $\partial f/\partial x$:** đạo hàm, đạo hàm riêng.
- **$\nabla f$, $H$:** gradient và Hessian (theo ngữ cảnh).
- **$\mathbb E[X]$, $\operatorname{Var}(X)$:** kỳ vọng và phương sai.
- **$A^T$, $A^{-1}$:** chuyển vị và nghịch đảo (nếu tồn tại).
- **$\|\mathbf x\|_2$:** chuẩn Euclid.
- **$P(A\mid B)$:** xác suất biến cố $A$ khi biết $B$.
- **$\theta$, $\eta$, $\lambda$:** tham số mô hình, tốc độ học và hệ số điều chuẩn (tùy ngữ cảnh).

# Phụ lục B. Tài liệu tham chiếu và ranh giới sử dụng

Tập 00 được biên soạn như một **văn bản giải thích và tổng hợp kiến thức toán học phổ thông/nền tảng**, không sao chép nguyên chương, hình hay bảng từ các sách thương mại. Để tiếp tục học Python và AI, có thể đọc các đầu sách người học đã cung cấp trong dự án: *Python Crash Course* (Eric Matthes), *Python for Data Analysis*, ấn bản 3 (Wes McKinney), *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow*, ấn bản 2 (Aurélien Géron), và *Deep Learning with Python* (François Chollet). Đây là **nguồn định hướng học tiếp**, không phải xác nhận rằng các ví dụ API trong những ấn bản cũ còn tương thích với mọi phiên bản phần mềm hiện hành.

**Giới hạn học thuật:** Các chứng minh trong Tập 00 được trình bày ở mức nhập môn với giả thiết cốt yếu. Một số kết quả nâng cao (ví dụ: quy tắc dây chuyền tổng quát, luật số lớn, lý thuyết tổng quát hóa và điều kiện trơn của gradient) được phát biểu hoặc phác thảo thay vì chứng minh đầy đủ theo giáo trình toán chuyên ngành.
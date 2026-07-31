
**Plotly（`fig` 对象）：**

|方法|作用|
|---|---|
|`fig.write_html('x.html')`|保存为网页，可交互|
|`fig.write_image('x.png')`|保存为图片（需装 kaleido）|
|`fig.write_json('x.json')`|保存图表配置|
|`fig.show()`|直接在浏览器打开|

---

**Matplotlib（`plt` / `fig` 对象）：**

|方法|作用|
|---|---|
|`plt.savefig('x.png')`|保存图片，支持 png/jpg/pdf/svg|
|`fig.savefig('x.png')`|同上，面向对象写法|
|`plt.show()`|弹窗显示|

---

**Pandas（`df` 对象）：**

|方法|作用|
|---|---|
|`df.to_csv('x.csv')`|保存为 CSV|
|`df.to_excel('x.xlsx')`|保存为 Excel|
|`df.to_json('x.json')`|保存为 JSON|
|`df.to_html('x.html')`|保存为网页表格|

---

**规律：**

- Plotly 用 `write_xxx()`
- Matplotlib 用 `savefig()`
- Pandas 用 `to_xxx()`
- pathlib 用 `write_text()` / `write_bytes()`

不同库的命名习惯不一样，记住各自的前缀就行。



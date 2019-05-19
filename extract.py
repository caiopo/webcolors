import re

groups = re.compile(r'<tr.*?>(.*?)<\/tr>', re.S)
tags = re.compile(r'<code>(.*)<\/code>')


def get_colors():
    for g in groups.findall(html):
        code_tags = tags.findall(g)
        if len(code_tags) != 3:
            continue

        name = code_tags[0]
        hexcode = ''.join(code_tags[1].split('&nbsp;'))

        yield (name, hexcode)


def main():
    for (name, hexcode) in get_colors():
        name = name[0].lower() + name[1:]

        print(f'static const {name} = Color(0xFF{hexcode});')


html = '''
<table style="font-size:90%; display: inline;" cellpadding="4">

<tbody><tr style="vertical-align:top;">
<td>
</td></tr>
<tr>
<th style="background:lightgrey" rowspan="2"><a href="/wiki/HTML" title="HTML">HTML</a> name
</th>
<th style="background:lightgrey" colspan="2"><a href="/wiki/RGB_color_model" title="RGB color model"><code>R &nbsp; G &nbsp; B</code></a>
</th></tr>
<tr>
<th style="background:lightgrey"><a href="/wiki/Hexadecimal" title="Hexadecimal"><code>Hex</code></a>
</th>
<th style="background:lightgrey"><code>Decimal</code>
</th></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Pink colors</b></span>
</td></tr>
<tr style="background:pink;color:black">
<td><code>Pink</code></td>
<td><code>FF&nbsp;C0&nbsp;CB</code></td>
<td><code>255&nbsp;192&nbsp;203</code>
</td></tr>
<tr style="background:lightpink;color:black">
<td><code>LightPink</code></td>
<td><code>FF&nbsp;B6&nbsp;C1</code></td>
<td><code>255&nbsp;182&nbsp;193</code>
</td></tr>
<tr style="background:hotpink;color:white">
<td><code>HotPink</code></td>
<td><code>FF&nbsp;69&nbsp;B4</code></td>
<td><code>255&nbsp;105&nbsp;180</code>
</td></tr>
<tr style="background:deeppink;color:white">
<td><code>DeepPink</code></td>
<td><code>FF&nbsp;14&nbsp;93</code></td>
<td><code>255&nbsp;&nbsp;20&nbsp;147</code>
</td></tr>
<tr style="background:palevioletred;color:white">
<td><code>PaleVioletRed</code></td>
<td><code>DB&nbsp;70&nbsp;93</code></td>
<td><code>219&nbsp;112&nbsp;147</code>
</td></tr>
<tr style="background:mediumvioletred;color:white">
<td><code>MediumVioletRed</code></td>
<td><code>C7&nbsp;15&nbsp;85</code></td>
<td><code>199&nbsp;&nbsp;21&nbsp;133</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Red colors</b></span>
</td></tr>
<tr style="background:lightsalmon;color:black">
<td><code>LightSalmon</code></td>
<td><code>FF&nbsp;A0&nbsp;7A</code></td>
<td><code>255&nbsp;160&nbsp;122</code>
</td></tr>
<tr style="background:salmon;color:black">
<td><code>Salmon</code></td>
<td><code>FA&nbsp;80&nbsp;72</code></td>
<td><code>250&nbsp;128&nbsp;114</code>
</td></tr>
<tr style="background:darksalmon;color:black">
<td><code>DarkSalmon</code></td>
<td><code>E9&nbsp;96&nbsp;7A</code></td>
<td><code>233&nbsp;150&nbsp;122</code>
</td></tr>
<tr style="background:lightcoral;color:black">
<td><code>LightCoral</code></td>
<td><code>F0&nbsp;80&nbsp;80</code></td>
<td><code>240&nbsp;128&nbsp;128</code>
</td></tr>
<tr style="background:indianred;color:white">
<td><code>IndianRed</code></td>
<td><code>CD&nbsp;5C&nbsp;5C</code></td>
<td><code>205&nbsp;&nbsp;92&nbsp;&nbsp;92</code>
</td></tr>
<tr style="background:crimson;color:white;color:white">
<td><code>Crimson</code></td>
<td><code>DC&nbsp;14&nbsp;3C</code></td>
<td><code>220&nbsp;&nbsp;20&nbsp;&nbsp;60</code>
</td></tr>
<tr style="background:firebrick;color:white">
<td><code>Firebrick</code></td>
<td><code>B2&nbsp;22&nbsp;22</code></td>
<td><code>178&nbsp;&nbsp;34&nbsp;&nbsp;34</code>
</td></tr>
<tr style="background:darkred;color:white">
<td><code>DarkRed</code></td>
<td><code>8B&nbsp;00&nbsp;00</code></td>
<td><code>139&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:red;color:white">
<td><code>Red</code></td>
<td><code>FF&nbsp;00&nbsp;00</code></td>
<td><code>255&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Orange colors</b></span>
</td></tr>
<tr style="background:orangered;color:white">
<td><code>OrangeRed</code></td>
<td><code>FF&nbsp;45&nbsp;00</code></td>
<td><code>255&nbsp;&nbsp;69&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:tomato;color:white">
<td><code>Tomato</code></td>
<td><code>FF&nbsp;63&nbsp;47</code></td>
<td><code>255&nbsp;&nbsp;99&nbsp;&nbsp;71</code>
</td></tr>
<tr style="background:coral;color:black">
<td><code>Coral</code></td>
<td><code>FF&nbsp;7F&nbsp;50</code></td>
<td><code>255&nbsp;127&nbsp;&nbsp;80</code>
</td></tr>
<tr style="background:darkorange;color:black">
<td><code>DarkOrange</code></td>
<td><code>FF&nbsp;8C&nbsp;00</code></td>
<td><code>255&nbsp;140&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:orange;color:black">
<td><code>Orange</code></td>
<td><code>FF&nbsp;A5&nbsp;00</code></td>
<td><code>255&nbsp;165&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Yellow colors</b></span>
</td></tr>
<tr style="background:yellow;color:black">
<td><code>Yellow</code></td>
<td><code>FF&nbsp;FF&nbsp;00</code></td>
<td><code>255&nbsp;255&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:lightyellow;color:black">
<td><code>LightYellow</code></td>
<td><code>FF&nbsp;FF&nbsp;E0</code></td>
<td><code>255&nbsp;255&nbsp;224</code>
</td></tr>
<tr style="background:lemonchiffon;color:black">
<td><code>LemonChiffon</code></td>
<td><code>FF&nbsp;FA&nbsp;CD</code></td>
<td><code>255&nbsp;250&nbsp;205</code>
</td></tr>
<tr style="background:lightgoldenrodyellow;color:black">
<td><code style="margin-right:1em;">LightGoldenrodYellow</code>&nbsp;</td>
<td><code>FA&nbsp;FA&nbsp;D2</code></td>
<td><code>250&nbsp;250&nbsp;210</code>
</td></tr>
<tr style="background:papayawhip;color:black">
<td><code>PapayaWhip</code></td>
<td><code>FF&nbsp;EF&nbsp;D5</code></td>
<td><code>255&nbsp;239&nbsp;213</code>
</td></tr>
<tr style="background:moccasin;color:black">
<td><code>Moccasin</code></td>
<td><code>FF&nbsp;E4&nbsp;B5</code></td>
<td><code>255&nbsp;228&nbsp;181</code>
</td></tr>
<tr style="background:peachpuff;color:black">
<td><code>PeachPuff</code></td>
<td><code>FF&nbsp;DA&nbsp;B9</code></td>
<td><code>255&nbsp;218&nbsp;185</code>
</td></tr>
<tr style="background:palegoldenrod;color:black">
<td><code>PaleGoldenrod</code></td>
<td><code>EE&nbsp;E8&nbsp;AA</code></td>
<td><code>238&nbsp;232&nbsp;170</code>
</td></tr>
<tr style="background:khaki;color:black">
<td><code>Khaki</code></td>
<td><code>F0&nbsp;E6&nbsp;8C</code></td>
<td><code>240&nbsp;230&nbsp;140</code>
</td></tr>
<tr style="background:darkkhaki;color:black">
<td><code>DarkKhaki</code></td>
<td><code>BD&nbsp;B7&nbsp;6B</code></td>
<td><code>189&nbsp;183&nbsp;107</code>
</td></tr>
<tr style="background:gold;color:black">
<td><code>Gold</code></td>
<td><code>FF&nbsp;D7&nbsp;00</code></td>
<td><code>255&nbsp;215&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Brown colors</b></span>
</td></tr>
<tr style="background:cornsilk;color:black">
<td><code>Cornsilk</code></td>
<td><code>FF&nbsp;F8&nbsp;DC</code></td>
<td><code>255&nbsp;248&nbsp;220</code>
</td></tr>
<tr style="background:blanchedalmond;color:black">
<td><code>BlanchedAlmond</code></td>
<td><code>FF&nbsp;EB&nbsp;CD</code></td>
<td><code>255&nbsp;235&nbsp;205</code>
</td></tr>
<tr style="background:bisque;color:black">
<td><code>Bisque</code></td>
<td><code>FF&nbsp;E4&nbsp;C4</code></td>
<td><code>255&nbsp;228&nbsp;196</code>
</td></tr>
<tr style="background:navajowhite;color:black">
<td><code>NavajoWhite</code></td>
<td><code>FF&nbsp;DE&nbsp;AD</code></td>
<td><code>255&nbsp;222&nbsp;173</code>
</td></tr>
<tr style="background:wheat;color:black">
<td><code>Wheat</code></td>
<td><code>F5&nbsp;DE&nbsp;B3</code></td>
<td><code>245&nbsp;222&nbsp;179</code>
</td></tr>
<tr style="background:burlywood;color:black">
<td><code>Burlywood</code></td>
<td><code>DE&nbsp;B8&nbsp;87</code></td>
<td><code>222&nbsp;184&nbsp;135</code>
</td></tr>
<tr style="background:tan;color:black">
<td><code>Tan</code></td>
<td><code>D2&nbsp;B4&nbsp;8C</code></td>
<td><code>210&nbsp;180&nbsp;140</code>
</td></tr>
<tr style="background:rosybrown;color:black">
<td><code>RosyBrown</code></td>
<td><code>BC&nbsp;8F&nbsp;8F</code></td>
<td><code>188&nbsp;143&nbsp;143</code>
</td></tr>
<tr style="background:sandybrown;color:black">
<td><code>SandyBrown</code></td>
<td><code>F4&nbsp;A4&nbsp;60</code></td>
<td><code>244&nbsp;164&nbsp;&nbsp;96</code>
</td></tr>
<tr style="background:goldenrod;color:black">
<td><code>Goldenrod</code></td>
<td><code>DA&nbsp;A5&nbsp;20</code></td>
<td><code>218&nbsp;165&nbsp;&nbsp;32</code>
</td></tr>
<tr style="background:darkgoldenrod;color:black">
<td><code>DarkGoldenrod</code></td>
<td><code>B8&nbsp;86&nbsp;0B</code></td>
<td><code>184&nbsp;134&nbsp;&nbsp;11</code>
</td></tr>
<tr style="background:Peru;color:black">
<td><code>Peru</code></td>
<td><code>CD&nbsp;85&nbsp;3F</code></td>
<td><code>205&nbsp;133&nbsp;&nbsp;63</code>
</td></tr>
<tr style="background:chocolate;color:white">
<td><code>Chocolate</code></td>
<td><code>D2&nbsp;69&nbsp;1E</code></td>
<td><code>210&nbsp;105&nbsp;&nbsp;30</code>
</td></tr>
<tr style="background:saddlebrown;color:white">
<td><code>SaddleBrown</code></td>
<td><code>8B&nbsp;45&nbsp;13</code></td>
<td><code>139&nbsp;&nbsp;69&nbsp;&nbsp;19</code>
</td></tr>
<tr style="background:sienna;color:white">
<td><code>Sienna</code></td>
<td><code>A0&nbsp;52&nbsp;2D</code></td>
<td><code>160&nbsp;&nbsp;82&nbsp;&nbsp;45</code>
</td></tr>
<tr style="background:brown;color:white">
<td><code>Brown</code></td>
<td><code>A5&nbsp;2A&nbsp;2A</code></td>
<td><code>165&nbsp;&nbsp;42&nbsp;&nbsp;42</code>
</td></tr>
<tr style="background:maroon;color:white">
<td><code>Maroon</code></td>
<td><code>80&nbsp;00&nbsp;00</code></td>
<td><code>128&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0</code>
</td></tr></tbody></table>

<table style="font-size:90%; display: inline;" cellpadding="4">

<tbody><tr style="vertical-align:top;">
<td>
</td></tr>
<tr>
<th style="background:lightgrey" rowspan="2"><a href="/wiki/HTML" title="HTML">HTML</a> name
</th>
<th style="background:lightgrey" colspan="2"><a href="/wiki/RGB_color_model" title="RGB color model"><code>R &nbsp; G &nbsp; B</code></a>
</th></tr>
<tr>
<th style="background:lightgrey"><a href="/wiki/Hexadecimal" title="Hexadecimal"><code>Hex</code></a>
</th>
<th style="background:lightgrey"><code>Decimal</code>
</th></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Green colors</b></span>
</td></tr>
<tr style="background:darkolivegreen;color:white">
<td><code>DarkOliveGreen</code></td>
<td><code>55&nbsp;6B&nbsp;2F</code></td>
<td><code>&nbsp;85&nbsp;107&nbsp;&nbsp;47</code>
</td></tr>
<tr style="background:olive;color:white">
<td><code>Olive</code></td>
<td><code>80&nbsp;80&nbsp;00</code></td>
<td><code>128&nbsp;128&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:olivedrab;color:white">
<td><code>OliveDrab</code></td>
<td><code>6B&nbsp;8E&nbsp;23</code></td>
<td><code>107&nbsp;142&nbsp;&nbsp;35</code>
</td></tr>
<tr style="background:yellowgreen;color:black">
<td><code>YellowGreen</code></td>
<td><code>9A&nbsp;CD&nbsp;32</code></td>
<td><code>154&nbsp;205&nbsp;&nbsp;50</code>
</td></tr>
<tr style="background:limegreen;color:black">
<td><code>LimeGreen</code></td>
<td><code>32&nbsp;CD&nbsp;32</code></td>
<td><code>&nbsp;50&nbsp;205&nbsp;&nbsp;50</code>
</td></tr>
<tr style="background:lime;color:black">
<td><code>Lime</code></td>
<td><code>00&nbsp;FF&nbsp;00</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;255&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:lawngreen;color:black">
<td><code>LawnGreen</code></td>
<td><code>7C&nbsp;FC&nbsp;00</code></td>
<td><code>124&nbsp;252&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:chartreuse;color:black">
<td><code>Chartreuse</code></td>
<td><code>7F&nbsp;FF&nbsp;00</code></td>
<td><code>127&nbsp;255&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:greenyellow;color:black">
<td><code>GreenYellow</code></td>
<td><code>AD&nbsp;FF&nbsp;2F</code></td>
<td><code>173&nbsp;255&nbsp;&nbsp;47</code>
</td></tr>
<tr style="background:springgreen;color:black">
<td><code>SpringGreen</code></td>
<td><code>00&nbsp;FF&nbsp;7F</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;255&nbsp;127</code>
</td></tr>
<tr style="background:mediumspringgreen;color:black">
<td><code style="margin-right:2em;">MediumSpringGreen</code>&nbsp;</td>
<td><code>00&nbsp;FA&nbsp;9A</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;250&nbsp;154</code>
</td></tr>
<tr style="background:lightgreen;color:black">
<td><code>LightGreen</code></td>
<td><code>90&nbsp;EE&nbsp;90</code></td>
<td><code>144&nbsp;238&nbsp;144</code>
</td></tr>
<tr style="background:palegreen;color:black">
<td><code>PaleGreen</code></td>
<td><code>98&nbsp;FB&nbsp;98</code></td>
<td><code>152&nbsp;251&nbsp;152</code>
</td></tr>
<tr style="background:darkseagreen;color:black">
<td><code>DarkSeaGreen</code></td>
<td><code>8F&nbsp;BC&nbsp;8F</code></td>
<td><code>143&nbsp;188&nbsp;143</code>
</td></tr>
<tr style="background:mediumaquamarine;color:black">
<td><code>MediumAquamarine</code></td>
<td><code>66&nbsp;CD&nbsp;AA</code></td>
<td><code>102&nbsp;205&nbsp;170</code>
</td></tr>
<tr style="background:mediumseagreen;color:black">
<td><code>MediumSeaGreen</code></td>
<td><code>3C&nbsp;B3&nbsp;71</code></td>
<td><code>&nbsp;60&nbsp;179&nbsp;113</code>
</td></tr>
<tr style="background:seagreen;color:white">
<td><code>SeaGreen</code></td>
<td><code>2E&nbsp;8B&nbsp;57</code></td>
<td><code>&nbsp;46&nbsp;139&nbsp;&nbsp;87</code>
</td></tr>
<tr style="background:forestgreen;color:white">
<td><code>ForestGreen</code></td>
<td><code>22&nbsp;8B&nbsp;22</code></td>
<td><code>&nbsp;34&nbsp;139&nbsp;&nbsp;34</code>
</td></tr>
<tr style="background:green;color:white">
<td><code>Green</code></td>
<td><code>00&nbsp;80&nbsp;00</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;128&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr style="background:darkgreen;color:white">
<td><code>DarkGreen</code></td>
<td><code>00&nbsp;64&nbsp;00</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;100&nbsp;&nbsp;&nbsp;0</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Cyan colors</b></span>
</td></tr>
<tr style="background:aqua;color:black">
<td><code>Aqua</code></td>
<td><code>00&nbsp;FF&nbsp;FF</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;255&nbsp;255</code>
</td></tr>
<tr style="background:cyan;color:black">
<td><code>Cyan</code></td>
<td><code>00&nbsp;FF&nbsp;FF</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;255&nbsp;255</code>
</td></tr>
<tr style="background:lightcyan;color:black">
<td><code>LightCyan</code></td>
<td><code>E0&nbsp;FF&nbsp;FF</code></td>
<td><code>224&nbsp;255&nbsp;255</code>
</td></tr>
<tr style="background:paleturquoise;color:black">
<td><code>PaleTurquoise</code></td>
<td><code>AF&nbsp;EE&nbsp;EE</code></td>
<td><code>175&nbsp;238&nbsp;238</code>
</td></tr>
<tr style="background:aquamarine;color:black">
<td><code>Aquamarine</code></td>
<td><code>7F&nbsp;FF&nbsp;D4</code></td>
<td><code>127&nbsp;255&nbsp;212</code>
</td></tr>
<tr style="background:turquoise;color:black">
<td><code>Turquoise</code></td>
<td><code>40&nbsp;E0&nbsp;D0</code></td>
<td><code>&nbsp;64&nbsp;224&nbsp;208</code>
</td></tr>
<tr style="background:mediumturquoise;color:black">
<td><code>MediumTurquoise</code></td>
<td><code>48&nbsp;D1&nbsp;CC</code></td>
<td><code>&nbsp;72&nbsp;209&nbsp;204</code>
</td></tr>
<tr style="background:darkturquoise;color:black">
<td><code>DarkTurquoise</code></td>
<td><code>00&nbsp;CE&nbsp;D1</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;206&nbsp;209</code>
</td></tr>
<tr style="background:lightseagreen;color:black">
<td><code>LightSeaGreen</code></td>
<td><code>20&nbsp;B2&nbsp;AA</code></td>
<td><code>&nbsp;32&nbsp;178&nbsp;170</code>
</td></tr>
<tr style="background:cadetblue;color:white">
<td><code>CadetBlue</code></td>
<td><code>5F&nbsp;9E&nbsp;A0</code></td>
<td><code>&nbsp;95&nbsp;158&nbsp;160</code>
</td></tr>
<tr style="background:darkcyan;color:white">
<td><code>DarkCyan</code></td>
<td><code>00&nbsp;8B&nbsp;8B</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;139&nbsp;139</code>
</td></tr>
<tr style="background:teal;color:white">
<td><code>Teal</code></td>
<td><code>00&nbsp;80&nbsp;80</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;128&nbsp;128</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Blue colors</b></span>
</td></tr>
<tr style="background:lightsteelblue;color:black">
<td><code>LightSteelBlue</code></td>
<td><code>B0&nbsp;C4&nbsp;DE</code></td>
<td><code>176&nbsp;196&nbsp;222</code>
</td></tr>
<tr style="background:powderblue;color:black">
<td><code>PowderBlue</code></td>
<td><code>B0&nbsp;E0&nbsp;E6</code></td>
<td><code>176&nbsp;224&nbsp;230</code>
</td></tr>
<tr style="background:lightblue;color:black">
<td><code>LightBlue</code></td>
<td><code>AD&nbsp;D8&nbsp;E6</code></td>
<td><code>173&nbsp;216&nbsp;230</code>
</td></tr>
<tr style="background:skyblue;color:black">
<td><code>SkyBlue</code></td>
<td><code>87&nbsp;CE&nbsp;EB</code></td>
<td><code>135&nbsp;206&nbsp;235</code>
</td></tr>
<tr style="background:lightskyblue;color:black">
<td><code>LightSkyBlue</code></td>
<td><code>87&nbsp;CE&nbsp;FA</code></td>
<td><code>135&nbsp;206&nbsp;250</code>
</td></tr>
<tr style="background:deepskyblue;color:black">
<td><code>DeepSkyBlue</code></td>
<td><code>00&nbsp;BF&nbsp;FF</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;191&nbsp;255</code>
</td></tr>
<tr style="background:dodgerblue;color:black">
<td><code>DodgerBlue</code></td>
<td><code>1E&nbsp;90&nbsp;FF</code></td>
<td><code>&nbsp;30&nbsp;144&nbsp;255</code>
</td></tr>
<tr style="background:cornflowerblue;color:black">
<td><code>CornflowerBlue</code></td>
<td><code>64&nbsp;95&nbsp;ED</code></td>
<td><code>100&nbsp;149&nbsp;237</code>
</td></tr>
<tr style="background:steelblue;color:white">
<td><code>SteelBlue</code></td>
<td><code>46&nbsp;82&nbsp;B4</code></td>
<td><code>&nbsp;70&nbsp;130&nbsp;180</code>
</td></tr>
<tr style="background:royalblue;color:white">
<td><code>RoyalBlue</code></td>
<td><code>41&nbsp;69&nbsp;E1</code></td>
<td><code>&nbsp;65&nbsp;105&nbsp;225</code>
</td></tr>
<tr style="background:blue;color:white">
<td><code>Blue</code></td>
<td><code>00&nbsp;00&nbsp;FF</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0&nbsp;255</code>
</td></tr>
<tr style="background:mediumblue;color:white">
<td><code>MediumBlue</code></td>
<td><code>00&nbsp;00&nbsp;CD</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0&nbsp;205</code>
</td></tr>
<tr style="background:darkblue;color:white">
<td><code>DarkBlue</code></td>
<td><code>00&nbsp;00&nbsp;8B</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0&nbsp;139</code>
</td></tr>
<tr style="background:navy;color:white">
<td><code>Navy</code></td>
<td><code>00&nbsp;00&nbsp;80</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0&nbsp;128</code>
</td></tr>
<tr style="background:midnightblue;color:white">
<td><code>MidnightBlue</code></td>
<td><code>19&nbsp;19&nbsp;70</code></td>
<td><code>&nbsp;25&nbsp;&nbsp;25&nbsp;112</code>
</td></tr></tbody></table>

<table style="font-size:90%; display: inline;" cellpadding="4">

<tbody><tr style="vertical-align:top;">
<td>
</td></tr>
<tr>
<th style="background:lightgrey" rowspan="2"><a href="/wiki/HTML" title="HTML">HTML</a> name
</th>
<th style="background:lightgrey" colspan="2"><a href="/wiki/RGB_color_model" title="RGB color model"><code>R &nbsp; G &nbsp; B</code></a>
</th></tr>
<tr>
<th style="background:lightgrey"><a href="/wiki/Hexadecimal" title="Hexadecimal"><code>Hex</code></a>
</th>
<th style="background:lightgrey"><code>Decimal</code>
</th></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Purple, violet, and magenta colors</b></span>
</td></tr>
<tr style="background:lavender;color:black">
<td><code>Lavender</code></td>
<td><code>E6&nbsp;E6&nbsp;FA</code></td>
<td><code>230&nbsp;230&nbsp;250</code>
</td></tr>
<tr style="background:thistle;color:black">
<td><code>Thistle</code></td>
<td><code>D8&nbsp;BF&nbsp;D8</code></td>
<td><code>216&nbsp;191&nbsp;216</code>
</td></tr>
<tr style="background:plum;color:black">
<td><code>Plum</code></td>
<td><code>DD&nbsp;A0&nbsp;DD</code></td>
<td><code>221&nbsp;160&nbsp;221</code>
</td></tr>
<tr style="background:violet;color:black">
<td><code>Violet</code></td>
<td><code>EE&nbsp;82&nbsp;EE</code></td>
<td><code>238&nbsp;130&nbsp;238</code>
</td></tr>
<tr style="background:orchid;color:black">
<td><code>Orchid</code></td>
<td><code>DA&nbsp;70&nbsp;D6</code></td>
<td><code>218&nbsp;112&nbsp;214</code>
</td></tr>
<tr style="background:fuchsia;color:black">
<td><code>Fuchsia</code></td>
<td><code>FF&nbsp;00&nbsp;FF</code></td>
<td><code>255&nbsp;&nbsp;&nbsp;0&nbsp;255</code>
</td></tr>
<tr style="background:Magenta;color:black">
<td><code>Magenta</code></td>
<td><code>FF&nbsp;00&nbsp;FF</code></td>
<td><code>255&nbsp;&nbsp;&nbsp;0&nbsp;255</code>
</td></tr>
<tr style="background:mediumorchid;color:white">
<td><code>MediumOrchid</code></td>
<td><code>BA&nbsp;55&nbsp;D3</code></td>
<td><code>186&nbsp;&nbsp;85&nbsp;211</code>
</td></tr>
<tr style="background:mediumpurple;color:white">
<td><code>MediumPurple</code></td>
<td><code>93&nbsp;70&nbsp;DB</code></td>
<td><code>147&nbsp;112&nbsp;219</code>
</td></tr>
<tr style="background:blueviolet;color:white">
<td><code>BlueViolet</code></td>
<td><code>8A&nbsp;2B&nbsp;E2</code></td>
<td><code>138&nbsp;&nbsp;43&nbsp;226</code>
</td></tr>
<tr style="background:darkviolet;color:white">
<td><code>DarkViolet</code></td>
<td><code>94&nbsp;00&nbsp;D3</code></td>
<td><code>148&nbsp;&nbsp;&nbsp;0&nbsp;211</code>
</td></tr>
<tr style="background:darkorchid;color:white">
<td><code>DarkOrchid</code></td>
<td><code>99&nbsp;32&nbsp;CC</code></td>
<td><code>153&nbsp;&nbsp;50&nbsp;204</code>
</td></tr>
<tr style="background:darkmagenta;color:white">
<td><code>DarkMagenta</code></td>
<td><code>8B&nbsp;00&nbsp;8B</code></td>
<td><code>139&nbsp;&nbsp;&nbsp;0&nbsp;139</code>
</td></tr>
<tr style="background:purple;color:white">
<td><code>Purple</code></td>
<td><code>80&nbsp;00&nbsp;80</code></td>
<td><code>128&nbsp;&nbsp;&nbsp;0&nbsp;128</code>
</td></tr>
<tr style="background:indigo;color:white">
<td><code>Indigo</code></td>
<td><code>4B&nbsp;00&nbsp;82</code></td>
<td><code>&nbsp;75&nbsp;&nbsp;&nbsp;0&nbsp;130</code>
</td></tr>
<tr style="background:darkslateblue;color:white">
<td><code>DarkSlateBlue</code></td>
<td><code>48&nbsp;3D&nbsp;8B</code></td>
<td><code>&nbsp;72&nbsp;&nbsp;61&nbsp;139</code>
</td></tr>
<tr style="background:slateblue;color:white">
<td><code>SlateBlue</code></td>
<td><code>6A&nbsp;5A&nbsp;CD</code></td>
<td><code>106&nbsp;&nbsp;90&nbsp;205</code>
</td></tr>
<tr style="background:mediumslateblue;color:white">
<td><code style="margin-right:2em;">MediumSlateBlue</code>&nbsp;</td>
<td><code>7B&nbsp;68&nbsp;EE</code></td>
<td><code>123&nbsp;104&nbsp;238</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>White colors</b></span>
</td></tr>
<tr style="background:white;color:black">
<td><code>White</code></td>
<td><code>FF&nbsp;FF&nbsp;FF</code></td>
<td><code>255&nbsp;255&nbsp;255</code>
</td></tr>
<tr style="background:snow;color:black">
<td><code>Snow</code></td>
<td><code>FF&nbsp;FA&nbsp;FA</code></td>
<td><code>255&nbsp;250&nbsp;250</code>
</td></tr>
<tr style="background:honeydew;color:black">
<td><code>Honeydew</code></td>
<td><code>F0&nbsp;FF&nbsp;F0</code></td>
<td><code>240&nbsp;255&nbsp;240</code>
</td></tr>
<tr style="background:mintcream;color:black">
<td><code>MintCream</code></td>
<td><code>F5&nbsp;FF&nbsp;FA</code></td>
<td><code>245&nbsp;255&nbsp;250</code>
</td></tr>
<tr style="background:azure;color:black">
<td><code>Azure</code></td>
<td><code>F0&nbsp;FF&nbsp;FF</code></td>
<td><code>240&nbsp;255&nbsp;255</code>
</td></tr>
<tr style="background:aliceblue;color:black">
<td><code>AliceBlue</code></td>
<td><code>F0&nbsp;F8&nbsp;FF</code></td>
<td><code>240&nbsp;248&nbsp;255</code>
</td></tr>
<tr style="background:ghostwhite;color:black">
<td><code>GhostWhite</code></td>
<td><code>F8&nbsp;F8&nbsp;FF</code></td>
<td><code>248&nbsp;248&nbsp;255</code>
</td></tr>
<tr style="background:whitesmoke;color:black">
<td><code>WhiteSmoke</code></td>
<td><code>F5&nbsp;F5&nbsp;F5</code></td>
<td><code>245&nbsp;245&nbsp;245</code>
</td></tr>
<tr style="background:seashell;color:black">
<td><code>Seashell</code></td>
<td><code>FF&nbsp;F5&nbsp;EE</code></td>
<td><code>255&nbsp;245&nbsp;238</code>
</td></tr>
<tr style="background:beige;color:black">
<td><code>Beige</code></td>
<td><code>F5&nbsp;F5&nbsp;DC</code></td>
<td><code>245&nbsp;245&nbsp;220</code>
</td></tr>
<tr style="background:oldlace;color:black">
<td><code>OldLace</code></td>
<td><code>FD&nbsp;F5&nbsp;E6</code></td>
<td><code>253&nbsp;245&nbsp;230</code>
</td></tr>
<tr style="background:floralwhite;color:black">
<td><code>FloralWhite</code></td>
<td><code>FF&nbsp;FA&nbsp;F0</code></td>
<td><code>255&nbsp;250&nbsp;240</code>
</td></tr>
<tr style="background:ivory;color:black">
<td><code>Ivory</code></td>
<td><code>FF&nbsp;FF&nbsp;F0</code></td>
<td><code>255&nbsp;255&nbsp;240</code>
</td></tr>
<tr style="background:antiquewhite;color:black">
<td><code>AntiqueWhite</code></td>
<td><code>FA&nbsp;EB&nbsp;D7</code></td>
<td><code>250&nbsp;235&nbsp;215</code>
</td></tr>
<tr style="background:linen;color:black">
<td><code>Linen</code></td>
<td><code>FA&nbsp;F0&nbsp;E6</code></td>
<td><code>250&nbsp;240&nbsp;230</code>
</td></tr>
<tr style="background:lavenderblush;color:black">
<td><code>LavenderBlush</code></td>
<td><code>FF&nbsp;F0&nbsp;F5</code></td>
<td><code>255&nbsp;240&nbsp;245</code>
</td></tr>
<tr style="background:mistyrose;color:black">
<td><code>MistyRose</code></td>
<td><code>FF&nbsp;E4&nbsp;E1</code></td>
<td><code>255&nbsp;228&nbsp;225</code>
</td></tr>
<tr>
<td colspan="3" style="background:whitesmoke;text-align:left;"><span style="font-size: 120%;"><b>Gray and black colors</b></span>
</td></tr>
<tr style="background:gainsboro;color:black">
<td><code>Gainsboro</code></td>
<td><code>DC&nbsp;DC&nbsp;DC</code></td>
<td><code>220&nbsp;220&nbsp;220</code>
</td></tr>
<tr style="background:lightgray; color:black;">
<td><code>LightGray</code></td>
<td><code>D3&nbsp;D3&nbsp;D3</code></td>
<td><code>211&nbsp;211&nbsp;211</code>
</td></tr>
<tr style="background:silver;color:black">
<td><code>Silver</code></td>
<td><code>C0&nbsp;C0&nbsp;C0</code></td>
<td><code>192&nbsp;192&nbsp;192</code>
</td></tr>
<tr style="background:darkgray; color:black;">
<td><code>DarkGray</code></td>
<td><code>A9&nbsp;A9&nbsp;A9</code></td>
<td><code>169&nbsp;169&nbsp;169</code>
</td></tr>
<tr style="background:gray;color:white">
<td><code>Gray</code></td>
<td><code>80&nbsp;80&nbsp;80</code></td>
<td><code>128&nbsp;128&nbsp;128</code>
</td></tr>
<tr style="background:dimgray; color:white;">
<td><code>DimGray</code></td>
<td><code>69&nbsp;69&nbsp;69</code></td>
<td><code>105&nbsp;105&nbsp;105</code>
</td></tr>
<tr style="background:lightslategray; color:white;">
<td><code>LightSlateGray</code></td>
<td><code>77&nbsp;88&nbsp;99</code></td>
<td><code>119&nbsp;136&nbsp;153</code>
</td></tr>
<tr style="background:slategray; color:white;">
<td><code>SlateGray</code></td>
<td><code>70&nbsp;80&nbsp;90</code></td>
<td><code>112&nbsp;128&nbsp;144</code>
</td></tr>
<tr style="background:darkslategray; color:white;">
<td><code>DarkSlateGray</code></td>
<td><code>2F&nbsp;4F&nbsp;4F</code></td>
<td><code>&nbsp;47&nbsp;&nbsp;79&nbsp;&nbsp;79</code>
</td></tr>
<tr style="background:black;color:white">
<td><code>Black</code></td>
<td><code>00&nbsp;00&nbsp;00</code></td>
<td><code>&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;0</code>
</td></tr></tbody></table>

'''


if __name__ == '__main__':
    main()

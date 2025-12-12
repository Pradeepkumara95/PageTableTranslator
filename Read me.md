----------Download EXE file-------------

Drive link:

https://drive.google.com/file/d/1YtgytfNB6QBijgF5XEn4Bu2TwfvruXEP/view?usp=sharing

GitHub:

https://github.com/Pradeepkumara95/PageTableTranslator

================================================================================================================

-- About this application --

Developer & Author : M.P.Pushpa kumara 422514886   (dec-2025)


### Page Table Translator with Tkinter GUI

This project is a simple desktop application that shows how memory address translation works in an operating system. Created using graphical interface made with Python and Tkinter. 

User Inputs 

    *page size

    *number of pages

    *number of frames

    *page-to-frame mappings

    *logical addresses. 

Pragrame calculates and displays the physical address or shows a page fault if the page is not mapped.


#### OBJECTIVE


Demonstrating paging and address translation

Understanding frame allocation

Visualizing page faults


#### Features

Easy-to-use GUI built with Tkinter.

Supports page size of 512 or 1024 bytes.

Allows 1 to 8 pages and 4 to 6 frames.

Page mapping area updates automatically when the number of pages is entered.

Accepts up to 10 logical addresses.

Shows detailed results including:

Logical address

Page number

Offset

Frame number

Physical address

Status (OK or Page Fault)



#### How It Works

1.Enter the page size.

2.Enter the number of pages.

    *Page mapping boxes will automatically appear.

3.Enter the number of physical frames.

4.Fill in the page mapping table:

    *Use a frame number (0 to frame\_count–1)

    *Use -1 for a page fault mapping

5.Enter one or more logical addresses in the 10 boxes.

6.Click TRANSLATE button.


#### 

#### Page Fault Handling

If a page has -1 mapped or if the page number is outside the valid range, the program popup error a page fault message.

-----Example------

Page = 2
Mapping = -1

    then, "Page Fault Occurred"

### 

### Software Requirements

Python 3.x

Tkinter (included with Python)

Exporting an .exe:- Auto-Py-to-Exe

Visual Studio Code

#### 


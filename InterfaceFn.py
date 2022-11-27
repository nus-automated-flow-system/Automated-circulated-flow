from asyncio import start_server
from mttkinter import mtTkinter as tk
from tkinter import ttk


class InterfaceFn:

        def autoprog_init():
                print("1")

        def autoprog_start():
                print("2")

        def autoprog_abort():
                None

        def autoprog_getfunc(self, init, start, abort):

                self.btn_init['command'] = init

                self.btn_start['command'] = start

                self.btn_abort['command'] = abort

        def instru_panel(name, num, tab_instru_status):

                globals()["fr_%s_status" % name] = tk.Frame(tab_instru_status, width=550, height=400)

                tab_instru_status.add(globals()["fr_%s_status" % name], text=name)

                for i in range(0, num):

                        for j in [0, 1]:

                                if i / 2 % 1 == 0:

                                        tk.Label(globals()["fr_%s_status" % name], text="%s %d" % (name, i + j + 1),
                                                 width=37, height=1).grid(row=i, column=j, padx=1, pady=1)

                                else:
                                        globals()["lbl_%s_%d_sta" % (name, i + j)] = tk.Label(
                                                globals()["fr_%s_status" % name], text="Null", anchor="w", width=37,
                                                height=int(40 / num) - 1, justify=tk.LEFT, relief=tk.GROOVE)

                                        globals()["lbl_%s_%d_sta" % (name, i + j)].grid(row=i, column=j, padx=1, pady=1)

        def myfunction(event):

                global canvas

                canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

        """Define window framework"""
        window = tk.Tk()
        window.title("Automation Program Execution")
        window.geometry("1200x700+150+80")
        window.rowconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.resizable(0, 0)

        """Define Command Panel"""

        fr_cmdPan = tk.Frame(window, width=600, height=700, relief=tk.FLAT, bd=2)
        fr_cmdPan.grid_propagate(0)
        fr_cmdPan.grid(row=0, column=2, padx=3, pady=3)
        fr_cmdPan.rowconfigure(2, weight=1)
        fr_cmdPan.columnconfigure(3, weight=9)

        tk.Label(fr_cmdPan, text="Command Sequence", height=1,
                 font=("calibri", 12, "bold"), relief=tk.FLAT).grid(row=0, column=0, padx=3, pady=3)

        fr_cmdBtn = tk.Frame(fr_cmdPan, relief=tk.FLAT, bd=2) 
        fr_cmdBtn.grid(row=3, column=0, padx=1, pady=1)

        btn_start = tk.Button(fr_cmdBtn, text="Start", width=15, command=autoprog_start)
        btn_start.grid(row=2, column=0, padx=15, pady=3)

        btn_pause = tk.Button(fr_cmdBtn, text="Pause", width=15, command=autoprog_start)
        btn_pause.grid(row=2, column=1, padx=15, pady=3)

        btn_resume = tk.Button(fr_cmdBtn, text="Resume", width=15, command=autoprog_start)
        btn_resume.grid(row=2, column=2, padx=15, pady=3)
        
        btn_abort = tk.Button(fr_cmdBtn, text="Abort", width=15, fg="red", command=autoprog_abort)
        btn_abort.grid(row=2, column=3, padx=15, pady=3)
        

        fr_canvas = tk.Frame(fr_cmdPan, width=585, height=600, relief=tk.GROOVE, bd=2)
        fr_canvas.grid(row=1, column=0, padx=3, pady=3, sticky="wn")

        canvas = tk.Canvas(fr_canvas, width=585, height=600, scrollregion=(0, 0, 585, 20000), confine=False, bg="white")
        canvas.pack()

        fr_cmdInt = tk.Frame(canvas, width=585, height=20000)
        fr_cmdInt.pack(side=tk.LEFT)
        fr_cmdInt.propagate(0)

        vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)
        vbar.place(x=568, width=20, height=600)
        vbar.configure(command=canvas.yview)

        canvas.create_window((280, 00), window=fr_cmdInt)
        canvas.configure(yscrollcommand=vbar.set, scrollregion=canvas.bbox("all"))

        tk.Label(fr_cmdInt, width=75, text='Successful example', bg="blue", anchor='w', justify=tk.LEFT).pack()
        tk.Label(fr_cmdInt, width=75, text='Failed example', bg="red", anchor='w', justify=tk.LEFT).pack()

        """Define Status Panel"""

        fr_output = tk.Frame(window, width=550, height=700, relief=tk.FLAT, bd=2)
        fr_output.grid(row=0, column=1, padx=5, pady=5)
        fr_output.grid_propagate(0)
        fr_output.rowconfigure(4, weight=1)
        fr_output.columnconfigure(0, weight=1)

        tk.Label(fr_output, text="Instruments Initialization", width=550, height=1, font=("calibri", 12, "bold")).grid(
                row=0, column=0, padx=3, pady=3)

        lbl_init = tk.Label(fr_output, anchor="w", width=550, height=10, justify=tk.LEFT, relief=tk.GROOVE)
        lbl_init.grid(row=1, column=0, padx=3, pady=3)

        btn_init = tk.Button(fr_output, width=8, text="Initialize", command=autoprog_init)
        btn_init.grid(row=2, column=0, padx=1, pady=1, sticky="ew")

        tk.Label(fr_output, text="Instruments Status", width=550, height=1, font=("calibri", 12, "bold")).grid(row=3,
                                                                                                               column=0,
                                                                                                               padx=3,
                                                                                                               pady=3)

        """ Define Instrument Status Panel """

        tab_instru_status = ttk.Notebook(fr_output, width=550, height=400)

        tab_instru_status.grid(row=4, column=0, padx=3, pady=3)

        ttk.Style().configure('TNotebook.Tab', width=10, height=2, anchor="ew")

        instru_panel("asiapump",4,tab_instru_status)
        instru_panel("sf10",4,tab_instru_status)
        instru_panel("milliGAT",4,tab_instru_status)
        instru_panel("oushisheng",4,tab_instru_status)
        instru_panel("heidolph",4,tab_instru_status)
        instru_panel("watson", 4, tab_instru_status)
        instru_panel("valve",6,tab_instru_status)
                          

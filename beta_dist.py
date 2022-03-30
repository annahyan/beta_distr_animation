## Adapted from Thomas Ott's https://www.t-ott.dev/2021/11/24/animating-normal-distributions

from manim import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
from scipy.stats import beta as beta_dist
import math

def PDF_beta(x, alpha, beta):
    '''
    General form of probability density function of univariate normal distribution
    '''
    
    val =  beta_dist.pdf(x, alpha, beta)
    if math.isnan(val) or math.isinf(val):
        val = 0
    return val



class AdjustAlpha(Scene):
    '''
    Scene to observe how adjustments to the mean of a normal distrubtion
    influences the shape of its probability density function
    '''

    def construct(self):
        ax = Axes(
            x_range = [0.01, 0.99, 0.01],
            y_range = [0, 2, 0.5] ,
            # x_range = [-5, 5, 1],
            # y_range = [0, 0.5, 0.1],

            # axis_config = {'include_numbers':True}
            axis_config={
                'color' : WHITE,
                'stroke_width' : 4,
                'include_numbers' : True,
                'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'include_sign' : True,
                    'color' : WHITE
                }
            }
        ).add_coordinates()

        # Initialize alpha (distribution mean) ValueTracker to 0
        alpha = ValueTracker(0)

        # Text to display distrubtion mean
        alpha_text = MathTex(r'\alpha = ').next_to(ax, UP, buff=0.2).set_color(YELLOW)
        # Always redraw the decimal value for alpha for each frame
        alpha_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(alpha.get_value())
            .next_to(alpha_text, RIGHT, buff=0.2)
            .set_color(YELLOW)
        )

        
        # Define PDF curve, always redraw for each frame
        curve = always_redraw(
            lambda: ax.plot(
                lambda x: PDF_beta(x, alpha.get_value(), 2), color=YELLOW)
        )

        # Start animation
        self.add(ax, alpha_text, alpha_value_text)
        self.play(Create(curve))
        self.play(
            alpha.animate.set_value(1),
            run_time=1,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            alpha.animate.set_value(10),
            run_time=1.5,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            alpha.animate.set_value(5),
            run_time=1,
            rate_func=rate_functions.smooth
        )
        self.play(Uncreate(curve))


class AdjustAlphaBeta(Scene):
    '''
    Scene to observe how adjustments to the mean of a normal distrubtion
    influences the shape of its probability density function
    '''

    def construct(self):
        ax = Axes(
            x_range = [0.01, 0.99, 0.1],
            y_range = [0, 2, 0.5] ,
            # x_range = [-5, 5, 1],
            # y_range = [0, 0.5, 0.1],

            # axis_config = {'include_numbers':True}
            axis_config={
                'color' : WHITE,
                'stroke_width' : 4,
                'include_numbers' : True,
                'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'include_sign' : True,
                    'color' : WHITE
                }
            }
        ).add_coordinates()

        # Initialize alpha (distribution mean) ValueTracker to 0
        alpha = ValueTracker(0)
        beta = ValueTracker(0)

        # Text to display distrubtion mean
        alpha_text = MathTex(r'\alpha = ').next_to(ax, UP, buff=0.2).set_color(YELLOW)
        # Always redraw the decimal value for alpha for each frame
        alpha_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(alpha.get_value())
            .next_to(alpha_text, RIGHT, buff=0.2)
            .set_color(YELLOW)
        )

        alpha_t = VGroup(alpha_text, alpha_value_text).arrange(RIGHT, buff=0.1)

        beta_text = MathTex(r'\beta = ').next_to(ax, UP, buff=0.2).set_color(YELLOW)
        # Always redraw the decimal value for beta for each frame
        beta_value_text = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(beta.get_value())
            .next_to(beta_text, RIGHT, buff=0.2)
            .set_color(YELLOW)
        )
        beta_t = VGroup(beta_text, beta_value_text).arrange(RIGHT, buff=0.1)


        text = VGroup(alpha_t, beta_t).arrange(UP, buff=0.2).move_to(UP*3.5)
        
        # Define PDF curve, always redraw for each frame
        curve = always_redraw(
            lambda: ax.plot(
                lambda x: PDF_beta(x, alpha.get_value(), beta.get_value()), color=YELLOW)
        )

        # Start animation
        # self.add(ax, alpha_text, beta_text, alpha_value_text)
        self.add(ax, text)
        self.play(Create(curve))
        self.play(
            alpha.animate.set_value(3),
            beta.animate.set_value(3),
            run_time=1,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            alpha.animate.set_value(3),
            beta.animate.set_value(1),
            run_time=1,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            alpha.animate.set_value(1),
            beta.animate.set_value(1),
            run_time=1.5,
            rate_func=rate_functions.smooth
        )
        self.wait()
        self.play(
            alpha.animate.set_value(0.1),
            beta.animate.set_value(0.1),
            run_time=1,
            rate_func=rate_functions.smooth
        )
        self.play(Uncreate(curve))


# From the command line :manim -pql beta_dist.py AdjustAlphaBeta

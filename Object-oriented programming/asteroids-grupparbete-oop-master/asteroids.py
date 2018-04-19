import sys
import random
import pygame
from pygame.locals import *

from game import Game
from ship import Ship
from star import Star
from bullet import Bullet
from asteroid import Asteroid
from time import time

class Asteroids( Game ):
    """
    Asteroids extends the base class Game to provide logic for the specifics of the game
    """
    def __init__(self, name, width, height):
        super().__init__( name, width, height )

        self.ship = Ship()  #  TODO: should create a Ship object here
        # TODO: should create asteroids
        self.asteroids=[Asteroid(), Asteroid(), Asteroid(), Asteroid()]   
        # TODO: should create stars
        i = 0
        starList = []
        while (i < random.randint(1, 500)):
            starList.append(Star())
            i += 1;
        self.stars = starList
        self.bullets = []


        #Start the font module                                                                                                                           
                                                                   
    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] and self.ship:
            self.ship.rotate(-4)
        if keys_pressed[K_RIGHT] and self.ship:
            self.ship.rotate(4)
        if keys_pressed[K_UP] and self.ship:
            self.ship.accelerate(0.2)
        if keys_pressed[K_DOWN] and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:
            if len(self.bullets) == 0:
                self.bullets.append( Bullet( self.ship.position.x, self.ship.position.y, 5, self.ship.rotation) )
            elif (time() - self.bullets[-1].timeCreated) > 0.35:
                self.bullets.append( Bullet( self.ship.position.x, self.ship.position.y, 5, self.ship.rotation) )

    def update_simulation(self):
        """
        update_simulation() causes all objects in the game to update themselves
        """
        super().update_simulation()

        if self.ship:
            self.ship.update( self.width, self.height )
        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
        for star in self.stars:
            star.update( self.width, self.height )
        # TODO: should probably call update on our bullet/bullets here
        for bullet in self.bullets:
            if bullet.ticks > 55:
                self.bullets.remove(bullet)
            else:
                bullet.update(self.width, self.height)
        # TODO: should probably work out how to remove a bullet when it gets old
        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()
        # Render the ship:
        if self.ship:
            self.ship.draw( self.screen )
        # Render all the stars, if any:
        for star in self.stars:
            star.draw( self.screen )
        # Render all the asteroids, if any:
        for asteroid in self.asteroids:
            asteroid.draw( self.screen )
        # Render all the bullet, if any:
        for bullet in self.bullets:
            bullet.draw( self.screen )
            bullet.ticks += 1


    def handle_collisions(self):
        """
        handle_collisions() should check:
            - if our ship has crashed into an asteroid (the ship gets destroyed - game over!)
            - if a bullet has hit an asteroid (the asteroid gets destroyed)
        :return: 
        """

        # TODO: implement collission detection,
        # using the collission detection methods in all of the shapes
        i = 0
        for asteroid in self.asteroids:
            if(asteroid.contains(self.ship.position)):
                print("YOU DIED")
                pygame.quit()

            for bullet in self.bullets:
                if(asteroid.contains(bullet.position)):
                    del self.asteroids[i]
                    self.bullets.remove(bullet)
                    return
            i = i + 1

        if len(self.asteroids) < 5:
            self.asteroids.append( Asteroid() )




        

/*
 * MinimaxPlayer.h
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */

#ifndef MINIMAXPLAYER_H
#define MINIMAXPLAYER_H

#include "OthelloBoard.h"
#include "Player.h"
#include <vector>

/**
 * This class represents an AI player that uses the Minimax algorithm to play the game
 * intelligently.
 */
struct MinimaxPlayer_node
	{
		/* data */
		int col;
		int row;
		int value;
	};
	
class MinimaxPlayer : public Player {
public:


	/**
	 * @param symb This is the symbol for the minimax player's pieces
	 */
	MinimaxPlayer(char symb);

	/**
	 * Destructor
	 */
	virtual ~MinimaxPlayer();

	/**
	 * @param b The board object for the current state of the board
	 * @param col Holds the return value for the column of the move
	 * @param row Holds the return value for the row of the move
	 */
	 void get_move(OthelloBoard* b, int& col, int& row);
	 void Min_max(OthelloBoard* b,int &col,int &row);
	 int checkfinal(OthelloBoard* b);
	 MinimaxPlayer_node Min_value(OthelloBoard* b,int istop=0);
	 MinimaxPlayer_node Max_value(OthelloBoard* b,int istop=0);
	 void Generate_Successor(OthelloBoard* b,char symb,int successor[16][2]);
	 int Cal_unity(OthelloBoard* b);
    /**
     * @return A copy of the MinimaxPlayer object
     * This is a virtual copy constructor
     */
	MinimaxPlayer* clone();

private:

};


#endif

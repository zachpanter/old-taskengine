/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package my.TaskEngine;

/**
 *
 * @author zpanter
 */
public class TaskEngine_Wizard 
{

    public TaskEngine_Wizard()
    {}

    public void createPhase()
    {}

    public void createNode()
    {}

    public void setNodeAsDefault(Node node)
    {
        int newDefaultNodeID = node.node_id;
        
        //Use database to find current default node, set as false
        node.setDefaultFlagTrue();
    }
    
}

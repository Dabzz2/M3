# tasks.py
from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
                Provide an overview of the current fiscal policy's impact on the economy, considering variables like {var1} and {var2}.

                {self.__tip_section()}

                Make sure to use the most recent data to provide an accurate analysis.
            """
            ),
            expected_output="An analysis of fiscal policy's effect on economic growth and unemployment.",
            agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
                Analyze the impact of recent monetary policy decisions in response to the fiscal policy analysis provided by the first agent.

                {self.__tip_section()}
            """
            ),
            expected_output="A contrasting viewpoint on how monetary policy influences inflation and economic stability.",
            agent=agent,
        )
    def task_3_name(self, agent):
        return Task(
        description=dedent(
            f"""
            Assess the impact of recent international trade policies in light of the fiscal and monetary analyses provided by the previous agents.

            {self.__tip_section()}
        """
        ),
        expected_output="An evaluation of how trade policies affect economic growth and international relations.",
        agent=agent,
    )
    def task_4_name(self, agent):
        return Task(
        description=dedent(
            f"""
            Assess the impact of recent international trade policies in light of the fiscal and monetary analyses provided by the previous agents by using the knowledge from neo4j.

            {self.__tip_section()}
        """
        ),
        expected_output="An evaluation of how trade policies affect economic growth and international relations.",
        agent=agent,
    )
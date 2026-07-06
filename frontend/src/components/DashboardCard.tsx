type Props = {

    title: string;

    value: string | number;

    color: string;

};

export default function DashboardCard({

    title,

    value,

    color,

}: Props) {

    return (

        <div

            style={{

                background: color,

                padding: 20,

                borderRadius: 12,

                color: "white",

                minWidth: 220,

            }}

        >

            <h3>{title}</h3>

            <h1>{value}</h1>

        </div>

    );

}